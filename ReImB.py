import math
import numpy as np
import const
import pandas as pd

def Gamma(E):
    gnGamma_0 = const.gnGamma_0*np.sqrt(E/np.abs(const.E_0))
    gnGamma_1 = const.gnGamma_1*np.sqrt(E/const.E_1)

    nGamma_0 = gnGamma_0/(2*const.g0)
    nGamma_1 = gnGamma_1/(2*const.g1)

    Gamma_0 = nGamma_0 + const.Gammagamma_0
    Gamma_1 = nGamma_1 + const.Gammagamma_1

    return nGamma_0, nGamma_1, Gamma_0, Gamma_1


def Gamma131(E):
    gnGamma_0 = const.gnGamma_0*np.sqrt(E)
    gnGamma_1 = const.gnGamma_1*np.sqrt(E/const.E_1)
    gnGamma_2 = const.gnGamma_2*np.sqrt(E/const.E_2)

    nGamma_0 = gnGamma_0/(2*const.g0)
    nGamma_1 = gnGamma_1/(2*const.g1)
    nGamma_2 = gnGamma_2/(2*const.g1)

    Gamma_0 = nGamma_0 + const.Gammagamma_0
    Gamma_1 = nGamma_1 + const.Gammagamma_1
    Gamma_2 = nGamma_2 + const.Gammagamma_2

    return nGamma_0, nGamma_1, nGamma_2, Gamma_0, Gamma_1, Gamma_2


def ImB_131Xe(E):
    nGamma_0, nGamma_1, nGamma_2, Gamma_0, Gamma_1, Gamma_2 = Gamma131(E)
    k = 0.6947*np.sqrt(E*10**3)*10**10
    
    return 3/(64*k)*(((4*nGamma_2*(2*k*(E-const.E_2)*const.R_0-(Gamma_2/2)))/((E-const.E_2)**2+(Gamma_2/2)**2))-((4*nGamma_0*(2*k*(E-const.E_0)*const.R_0-(Gamma_0/2)))/((E-const.E_0)**2+(Gamma_0/2)**2)))+3/(64*k)*((7*nGamma_1*Gamma_1)/(2*((E-const.E_1)**2+(Gamma_1/2)**2)))

def ImB_129(E):
    