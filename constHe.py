import numpy as np
import pandas as pd

P_He = 0.7
# p_He = 1.0
# rho_d_He = 20*2.686*10**19*10**4 #[m^-2]
rho_d_He = 60*2.686*10**19*10**4 #[m^-2]
dSigma_He = 276.4/10**28 #[m^2]

Pn = -np.tanh(P_He*rho_d_He*dSigma_He)