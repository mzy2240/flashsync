import streamsync as ss
import pandas as pd


def increment(state, value=None):
    state["counter"] += 1


ss.init_state({
    "counter": 0
})
ss.markdown('_this_ is **easy** to `use`.')
ss.markdown("***")
ss.latex(r"""T_{\mathrm{c}}=T_{\mathrm{a}}+\left(\frac{0.32}{8.91+2.0 V_{\mathrm{f}}}\right) G_{\mathrm{T}}""")
ss.code(r"""
def say_hello():
    print('Hello Naive UI')
""")
df = pd.util.testing.makeDataFrame()
ss.simple_table(df)
ss.text("The count is @counter.")
ss.button("Increment", handlers={"click": increment})

with ss.when(lambda state: state["counter"] >= 10 and state["counter"] < 20):
    ss.text("Well done on reaching 10, here's a trophy: 🏆. Keep going!")

with ss.when(lambda state: state["counter"] >= 20):
    ss.text("You've earned a gold medal for reaching 20 🥇")
