import streamsync as ss
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import time
import asyncio

df = pd.util.testing.makeDataFrame()


def increment(state, value=None):
    state["counter"] += 1

def ct(state, value=None):
    print("yeah")
    state["continue"] = True

def change(state, value=None):
    state["input"] = value

def download(state, value=None):
    for i in range(10):
        time.sleep(0.3)
        state["progress"] = 10*(i+1)
    state["spin"] = False



ss.init_state({
    "counter": 0,
    "message": "You're not mouseovering me", 
    "title": "Streamsync demo",
    "continue": False,
    "input": "",
    "progress": 0,
    "spin": True
})
# ss.init_state({"counter": 0})
# ss.image(r"https://www.tamu.edu/assets/images/TAM-Logo-white.png")
ss.image(r"C:\Users\test\OneDrive\Pictures\cps_architecture.PNG", width=300)
ss.input(placeholder="Test", handlers={"input": change})
ss.text("@input")

ss.button("Start download", handlers={"click": download})
# spin = ss.spin("@spin")
# ss.progressbar('@progress', to=spin)

col0, col1 = ss.grid(2)
ss.text("left", to=col0)
ss.text("right", to=col1)
card = ss.card("Title")
ss.text("Card content", to=card)

ss.button("Continue", handlers={"click": ct})
ss.markdown("***")
with ss.when(lambda state: state["continue"] == True):
    ss.text("You’ve had too many coffees.")
    ss.text("Oh really?")

    ss.text("That's awesome!!")
    ss.markdown("***")
    ss.text("WOW!!!")
    ss.latex(
        r"""T_{\mathrm{c}}=T_{\mathrm{a}}+\left(\frac{0.32}{8.91+2.0 V_{\mathrm{f}}}\right) G_{\mathrm{T}}""")
    ss.code(r"""
    def say_hello():
        print('Hello Naive UI')
    """)
    col0, col1 = ss.grid(2)
    ss.text("left1", to=col0)
    ss.text("right1", to=col1)


#     ss.simple_table(df)
#     ss.data_table(df)
#     ss.text("The count is @counter.")


ss.text("The count is @counter.")
ss.button("Increment", handlers={"click": increment})

with ss.when(lambda state: state["counter"] >= 10 and state["counter"] < 20):
    ss.text("Well done on reaching 10, here's a trophy: 🏆. Keep going!")

with ss.when(lambda state: state["counter"] >= 20):
    ss.text("You've earned a gold medal for reaching 20 🥇")


# def mouseover(state, value=None):
#     state["message"] = "You're mouseovering me."


# def mouseout(state, value=None):
#     state["message"] = "You're not mouseovering me"


# with ss.section():
#     ss.heading(
#         "@message", handlers={"mouseover": mouseover, "mouseout": mouseout})


# def replot(state, value):
#     filtered_data = [x for x in generated_data if x < int(value)]
#     fig, ax = plt.subplots()
#     ax.plot(filtered_data)
#     state["fig"] = fig


# mpl.use("Agg")
# generated_data = np.random.randint(1, 1000, 300)
# ss.init_state({"filter_value": 0, "fig": None})
# ss.slider("@filter_value", 0, 1000, handlers={"change": replot})
# ss.pyplot("@fig")
