import numpy as np
import matplotlib.pyplot as plt
import math
import const131
import const129
import constHe
import pandas as pd
import ReImB

def Gamma129(E):
    gnGamma_0 = 23.09*10**(-3)
    gnGamma_1 = 2.99*10**(-3)

    nGamma_0 = gnGamma_0/(2*const129.g0)
    nGamma_1 = gnGamma_1/(2*const129.g1)

    Gamma_0 = nGamma_0 + const129.Gammagamma_0
    Gamma_1 = nGamma_1 + const129.Gammagamma_1

    return nGamma_0, nGamma_1, Gamma_0, Gamma_1

def sigma_A(E):
    nGamma_0, nGamma_1, Gamma_0, Gamma_1 = Gamma129(E)
    k = 0.6947*np.sqrt(E*10**3)*10**10
    return 10**28*(-(np.pi/(2*k**2))*(nGamma_0*(2*k*(E-const129.E_0)*const129.R_0-Gamma_0/2)/((E-const129.E_0)**2+(Gamma_0/2)**2) + 3*nGamma_1*(2*k*(E-const129.E_1)*const129.R_0-Gamma_1/2)/((E-const129.E_1)**2+(Gamma_1/2)**2)) + 4*np.pi*const129.R_0**2)

E_values = np.linspace(2.5, 20, 1000)  

sigmaA_values = [ReImB.sigmaA129(E) for E in E_values]

plt.plot(E_values, sigmaA_values)
plt.xlabel('E (eV)')  
plt.ylabel('sigmaA(barn)')  
plt.title('sigmaA129')  
plt.grid(True)  

plt.yscale('log')  

plt.savefig('sigmaA_129Xe.png')  
plt.show()