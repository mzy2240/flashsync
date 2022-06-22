# FlashSync

Like Streamlit, but fast. A proof-of-concept framework built using Vue.js/Vite + Python/FastAPI + MSGPACK + WebSockets.

## Installation

```python
pip install flashsync
```


## Sample app

```python
import flashsync.flashsync as ss

def increment(state, value=None): # Event handler which receives a copy of session state as an argument
    state["counter"] += 1

ss.init_state({"counter": 0}) # State initialisation

ss.text("The count is @counter.") # Template strings with references to state values
ss.button("Increment", handlers={"click": increment}) # Linking components to event handlers

with ss.when(lambda state: state["counter"] >= 10 and state["counter"] < 20): # Conditional rendering
    ss.text("Well done on reaching 10, here's a trophy: 🏆. Keep going!")

with ss.when(lambda state: state["counter"] >= 20):
    ss.text("You've earned a gold medal for reaching 20 🥇")
```


## Authors

* **Zeyu Mao**

