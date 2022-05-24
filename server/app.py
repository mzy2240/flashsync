# fix windows registry stuff
import sys
import importlib
import copy
import ormsgpack
from starlette.responses import RedirectResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI, WebSocket, Request
import uvicorn
import mimetypes
mimetypes.add_type('application/javascript', '.js')
mimetypes.add_type('text/css', '.css')

# import flask
# import flask_sock


user_script = importlib.import_module(
    sys.argv[1])  # Dynamically import user script
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")


# Pack the initial state and components

@app.get("/api/init")
async def init():
    initial_state = user_script.ss.initial_state.state
    active_components = user_script.ss.get_active_components(initial_state)
    response_payload = {
        "state": initial_state,
        "components": active_components
    }

    return response_payload


# Listen to events. Keep the WebSockets stream open and waiting for forwarded events from the frontend.
# Call the event handlers. These will likely modify session state.
# Respond with state mutations and active components.


@app.websocket("/api/stream")
async def stream(websocket: WebSocket):
    await websocket.accept()
    session_state = copy.deepcopy(user_script.ss.initial_state)
    while True:
        raw = await websocket.receive()
        websocket._raise_on_disconnect(raw)
        text = raw["bytes"]
        data = ormsgpack.unpackb(text)
        type = data["type"]
        target_id = data["targetId"]
        value = data["value"]

        # Get active components. That is, components that don't depend on a conditioner (conditional rendering function)
        # or components for which their conditioner returns True.

        session_components = user_script.ss.get_active_components(
            session_state)

        # Trigger handler (component needs to be active in the session)

        session_components[target_id]["handlers"][type](session_state, value)

        # Reobtaining session components to account for state changes that may have caused components to become active/inactive

        session_components = user_script.ss.get_active_components(
            session_state)

        # orjson.dumps()
        msg = ormsgpack.packb({
            "mutations": session_state.mutations(),
            "components": session_components
        }, default=lambda x: True)

        # await websocket.send_text(msg.decode('utf-8'))
        await websocket.send_bytes(msg)


# Serve static files

@app.get("/")
async def read_index():
    return FileResponse('static/index.html')


@app.get("/{catchall:path}", response_class=FileResponse)
async def read_index(request: Request):
    # check first if requested file exists
    path = request.path_params["catchall"]
    file = "static/" + path
    return FileResponse(file)

# Start FastAPI

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)
