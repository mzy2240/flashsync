# FlashSync

Like Streamlit, but fast. A proof-of-concept framework built using Vue.js/Vite + Python/FastAPI + MSGPACK + WebSockets.

By avoiding a rerun of the whole script, FlashSync can react more than 70 times faster. This is all achieved while maintaining a similar syntax. This repository is a companion to the following Medium article (no paywall), which explains how FlashSync was built, the tests conducted and the implications: https://medium.com/@ramiromedina/like-streamlit-but-fast-enabling-low-latency-data-apps-948b95b098a2.

Please note that for the time being FlashSync isn't a viable, fully-fledged alternative to Streamlit, but rather a demonstration that a much faster alternative is possible. If there's some interest, I'll develop this into a viable alternative.

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

