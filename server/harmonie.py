import streamsync as ss
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

ss.heading(
    "Adaptive Routing for Improving Resilience of Cyber Physical Power System")

# ss.markdown("***")
ss.markdown(r"""
# Key points
* Self-healing network topology with adaptive routing
* Leverage the state estimation residues to improve the resilience of the network
* Validate the adaptive routing framework with large synthetic grid
* Test on single-point and multi-point False Data Injection (FDI) attacks and communication degradation cases
""")

card = ss.card("Background")
ss.text("test1", to=card)
ss.text("test2", to=card)
ss.text("test3", to=card)
# ss.text("Electric utilities have installed extensive supervisory control and data acquisition (SCADA) throughout\
#      the network to support computer-based systems. The data is used for numerous applications (e.g., system monitoring, \
#          economic system operation, security assessment, control of generation, etc…). ", to=card)
# ss.text("To provide reliable estimate of the existing system state, state estimator (SE) is widely used to all the caculation\
#      of the variables of interest with high confidence.", to=card)
# ss.text("One of the most classical approach is the weighted least square (WLS) method, which is to minimize the sum of the \
#     weighted squares of the estimated measurements from the true state, as shown below:", to=card)
# ss.latex(
#     r"""\min J(x)=\sum_{i=1}^{m} \frac{\left(z_{i}-h_{i}(x)\right)^{2}}{\sigma_{i}^{2}}""", to=card)
# ss.latex("where $m$ is the number of measurements, $z_{i}$ is the measured value, $h_{i}(x)$ is the estimated value, \
#     and $sigma_{i}$ is the measurement error.", to=card)
# ss.text("Bad Data Detection (BDD) is used to check if the weighted sum of the squares of these residuals has a Chi-square distribution", to=card)
# ss.latex(r"""r_{i}=z_{i}-h_{i}(\hat{x})""", to=card)

fdi = ss.card("False Data Injection (FDI)")