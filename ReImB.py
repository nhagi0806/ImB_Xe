import math
import numpy as np
import const131
import const129
import constHe
import pandas as pd

def Gamma129(E):
    gnGamma_0 = const129.gnGamma_0*np.sqrt(E/np.abs(const129.E_0))
    gnGamma_1 = const129.gnGamma_1*np.sqrt(E/const129.E_1)

    nGamma_0 = gnGamma_0/(2*const129.g0)
    nGamma_1 = gnGamma_1/(2*const129.g1)

    Gamma_0 = nGamma_0 + const129.Gammagamma_0
    Gamma_1 = nGamma_1 + const129.Gammagamma_1

    return nGamma_0, nGamma_1, Gamma_0, Gamma_1


def Gamma131(E):
    gnGamma_0 = const131.gnGamma_0*np.sqrt(E)
    gnGamma_1 = const131.gnGamma_1*np.sqrt(E/const131.E_1)
    gnGamma_2 = const131.gnGamma_2*np.sqrt(E/const131.E_2)

    nGamma_0 = gnGamma_0/(2*const131.g0)
    nGamma_1 = gnGamma_1/(2*const131.g1)
    nGamma_2 = gnGamma_2/(2*const131.g1)

    Gamma_0 = nGamma_0 + const131.Gammagamma_0
    Gamma_1 = nGamma_1 + const131.Gammagamma_1
    Gamma_2 = nGamma_2 + const131.Gammagamma_2

    return nGamma_0, nGamma_1, nGamma_2, Gamma_0, Gamma_1, Gamma_2

def ImB_131Xe(E):
    nGamma_0, nGamma_1, nGamma_2, Gamma_0, Gamma_1, Gamma_2 = Gamma131(E)
    k = 0.6947*np.sqrt(E*10**(-3))*10**10
    
    return 3/(64*k)*(((4*nGamma_2*(2*k*(E-const131.E_2)*const131.R_0-(Gamma_2/2)))/((E-const131.E_2)**2+(Gamma_2/2)**2))-((4*nGamma_0*(2*k*(E-const131.E_0)*const131.R_0-(Gamma_0/2)))/((E-const131.E_0)**2+(Gamma_0/2)**2)))+3/(64*k)*((7*nGamma_1*Gamma_1)/(2*((E-const131.E_1)**2+(Gamma_1/2)**2)))

def siggmaB131(E):
    k = 0.6947*np.sqrt(E*10**(-3))*10**10

    return (4*np.pi/k)*ImB_131Xe(E)*10**28     #スピン依存する断面積（barn） 

def siggmaB131abs(E):
    k = 0.6947*np.sqrt(E*10**(-3))*10**10

    return np.abs((4*np.pi/k)*ImB_131Xe(E)*10**28)     #スピン依存する断面積（barn） 

def ImB_129Xe(E):
    nGamma_0, nGamma_1, Gamma_0, Gamma_1 = Gamma129(E)
    k = 0.6947*np.sqrt(E*10**3)*10**10

    return 1/(8*k)*((nGamma_0*(2*k*(E-const129.E_0)*const129.R_0-(Gamma_0/2)))/((E-const129.E_0)**2+(Gamma_0/2)**2)-(nGamma_1*(2*k*(E-const129.E_1)*const129.R_0-(Gamma_1/2)))/((E-const129.E_1)**2+(Gamma_1/2)**2))

def siggmaB129(E):
    k = 0.6947*np.sqrt(E*10**3)*10**10
    return (4*np.pi/k)*ImB_129Xe(E)*10**(28)   #スピン依存する断面積（barn）

def ImA_129Xe(E):
    nGamma_0, nGamma_1, Gamma_0, Gamma_1 = Gamma129(E)
    k = 0.6947*np.sqrt(E*10**3)*10**10

    return -1/(8*k)*((nGamma_0*(2*k*(E-const129.E_0)*const129.R_0-(Gamma_0/2)))/((E-const129.E_0)**2+(Gamma_0/2)**2)+3*(nGamma_1*(2*k*(E-const129.E_1)*const129.R_0-(Gamma_1/2)))/((E-const129.E_1)**2+(Gamma_1/2)**2))

def siggmaA129(E):
    k = 0.6947*np.sqrt(E*10**3)*10**10
    
    return (4*np.pi/k)*ImA_129Xe(E)*10**(28)   #単位(barn)

def epsilon131(E):
    k = 0.6947*np.sqrt(E*10**3)*10**10
    return 0.17*np.tanh(4.2*10**(-4)*const131.num_131*5*10**(-2)*(4*np.pi/k)*ImB_131Xe(E))
    #return 1*np.tanh(1*const131.num_131*5*10**(-2)*(4*np.pi/k)*10**(-28)*ImB_131Xe(E))      #もし偏極率が１００％なら

def epsilon129(E):
    k = 0.6947*np.sqrt(E*10**(-3))*10**10
    return 0.17*np.tanh(1.9*10**(-2)*const129.num_129*10*10**(-2)*(4*np.pi/k)*ImB_129Xe(E))
    #return 0.17*np.tanh(0.17*const129.num_129*10*10**(-2)*(4*np.pi/k)*10**(-28)*ImB_129Xe(E))  #偏極率が１７％なら
    #return 1*np.tanh(1*const129.num_129*10*10**(-2)*(4*np.pi/k)*10**(-28)*ImB_129Xe(E))    #もし偏極率が１００％なら



