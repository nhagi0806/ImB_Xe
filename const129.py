import numpy as np
import pandas as pd

E_0=-21.81
E_1=9.57

gnGamma_0 = 23.09*10**(-3)*np.sqrt(np.abs(E_0)) #|E_0|eVでの2gGamma.
# gnGamma_0 = 23.09*10**(-3) # １eVでの2gGamma.
gnGamma_1 = 9.24*10**(-3) #E_1での2gGamma.

Gammagamma_0 = 121.6*10**(-3)
Gammagamma_1 = 116*10**(-3)

# g = (2J+1)/(2(2I+1))
g0 = 1/4
g1 = 3/4

R_0 = 4.7775*10**(-15)

mu_N = -9.6623651*10**(-27) #[J/T]
mu_N = mu_N/(1.62*10**(-19)) #[eV/T]
m_N = 9.3956542052*10**8 #[eV]
h_bar = 6.582119569*10**(-16) #[eV s]
c = 2.99792458*10**8 #[m/s]

p_129 = 1.0 #[atm]
num_129 = p_129*5.88*10**3*6.02*10**23/131.3 #[m^-3]
# # d_cell = 5*10**(-2)
d_cell = 10*10**(-2)




