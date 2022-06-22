import streamsync as ss
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

df = pd.util.testing.makeDataFrame()


def increment(state, value=None):
    state["counter"] += 1

def ct(state, value=None):
    print("yeah")
    state["continue"] = True


ss.init_state({
    "counter": 0,
    "message": "You're not mouseovering me", 
    "title": "Streamsync demo",
    "continue": False
})
# ss.init_state({"counter": 0})
col0, col1 = ss.grid(2)
ss.text("left", to=col0)
ss.text("right", to=col1)
card = ss.card("Title")
ss.text("Card content", to=card)

ss.button("Continue", handlers={"click": ct})
ss.markdown("***")
ss.text("After markdown")