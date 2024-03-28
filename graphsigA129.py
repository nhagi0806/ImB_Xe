import math
import numpy as np
import const129
import pandas as pd
import ReImB
import matplotlib.pyplot as plt

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