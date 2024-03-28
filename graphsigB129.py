import math
import numpy as np
import const129
import pandas as pd
import ReImB
import matplotlib.pyplot as plt

E_values = np.linspace(2.5, 20, 1000)  

sigmaB_values = [ReImB.sigmaB129(E) for E in E_values]

plt.plot(E_values, sigmaB_values)
plt.xlabel('E (eV)')  
plt.ylabel('sigmaB(barn)')  
plt.title('sigmaB129')  
plt.grid(True)  

plt.yscale('log') 

plt.savefig('sigmaB_129Xe.png')  
plt.show()