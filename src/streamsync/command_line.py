import streamsync.serve
import argparse
import os
import logging
import shutil


def main():
    parser = argparse.ArgumentParser(
        description="Run, edit or create a Streamsync app.")
    parser.add_argument("command", choices=[
                        "run", "edit", "create", "hello"])
    parser.add_argument(
        "path", nargs='?', help="Path to the app's folder")
    parser.add_argument(
        "--port", help="The port on which to run the server.")
    parser.add_argument(
        "--host", help="The host on which to run the server. Use 0.0.0.0 to share in your local network.")

    args = parser.parse_args()
    command = args.command
    default_port = 3006 if command in ("edit", "hello") else 3005
    port = int(args.port) if args.port else default_port        

    absolute_app_path = _get_absolute_app_path(
        args.path) if args.path else None
    
    if command in ("run", "edit") and args.path is None:
        logging.error("A path to a folder containing a Streamsync app is required. For example, streamsync edit my_app.")
        return
    
    default_host = "127.0.0.1"
    host = args.host if args.host else default_host

    if command in ("edit", "hello") and host != default_host:
        logging.warning("Streamsync has been enabled in edit mode with a host argument\nThis is enabled for local development purposes (such as a local VM).\nDon't expose Streamsync Builder to the Internet. We recommend using a SSH tunnel instead.")
        logging.warning("Streamsync Builder will only accept local requests (via HTTP origin header).")

    if command in ("edit"):

        # Builder is hardcoded to use default host (local)

        streamsync.serve.serve(
            absolute_app_path, mode="edit", port=port, host=host)
    if command in ("run"):
        streamsync.serve.serve(
            absolute_app_path, mode="run", port=port, host=host)
    elif command in ("hello"):
        create_app("hello", template_name="hello")
        streamsync.serve.serve("hello", mode="edit",
                               port=port, host=host)
    elif command in ("create"):
        create_app(absolute_app_path)


def create_app(app_path: str, template_name: str = "default"):
    server_path = os.path.dirname(__file__)
    template_path = os.path.join(server_path, "app_templates", template_name)
    shutil.copytree(template_path, app_path, dirs_exist_ok=True)


def _get_absolute_app_path(app_path: str):
    is_path_absolute = os.path.isabs(app_path)
    if is_path_absolute:
        return app_path
    else:
        return os.path.join(os.getcwd(), app_path)


if __name__ == "__main__":
    main()
