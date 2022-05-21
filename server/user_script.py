import streamsync as ss
import pandas as pd

df = pd.util.testing.makeDataFrame()

def increment(state, value=None):
    state["counter"] += 1


ss.init_state({
    "counter": 0
})
grid = ss.grid(2)
ss.text("left", grid=grid, col=0)
ss.text("right", grid=grid, col=1)
# ss.text("right", to=grid, col=1)
ss.markdown('_this_ is **easy** to `use`.')

ss.markdown("***")
ss.latex(r"""T_{\mathrm{c}}=T_{\mathrm{a}}+\left(\frac{0.32}{8.91+2.0 V_{\mathrm{f}}}\right) G_{\mathrm{T}}""")
ss.code(r"""
def say_hello():
    print('Hello Naive UI')
""")


ss.simple_table(df)
ss.data_table(df)
ss.text("The count is @counter.")
ss.button("Increment", handlers={"click": increment})

with ss.when(lambda state: state["counter"] >= 10 and state["counter"] < 20):
    ss.text("Well done on reaching 10, here's a trophy: 🏆. Keep going!")

with ss.when(lambda state: state["counter"] >= 20):
    ss.text("You've earned a gold medal for reaching 20 🥇")
