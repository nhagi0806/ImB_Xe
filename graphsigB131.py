import math
import numpy as np
import const129
import pandas as pd
import ReImB
import matplotlib.pyplot as plt

E_values = np.linspace(1, 20, 1000) 

sigmaB_values = [ReImB.sigmaB131(E) for E in E_values]

plt.plot(E_values, sigmaB_values)
plt.xlabel('E (eV)')  
plt.ylabel('sigmaB(barn)')  
plt.title('sigmaB131')  
plt.grid(True)  

closest_index = np.argmin(np.abs(E_values - 14.41))

plt.text(14.41 + 0.1, sigmaB_values[closest_index], f'{sigmaB_values[closest_index]:.3g}', fontsize=10, ha='left', va='bottom')

plt.savefig('sigmaB_131Xe.png')  
plt.show()