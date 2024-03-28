import math
import numpy as np
import const129
import pandas as pd
import ReImB
import matplotlib.pyplot as plt

E_values = np.linspace(1, 20, 1000)  
#E_values = np.linspace(1, 4, 1000)

sigmaB_values = [ReImB.sigmaB131abs(E) for E in E_values]

plt.plot(E_values, sigmaB_values)
plt.xlabel('E (eV)')  
plt.ylabel('sigmaBabs(barn)')  
plt.title('sigmaB131(abs)')  
plt.grid(True)  

plt.yscale('log') 

closest_index = np.argmin(np.abs(E_values - 14.41))
closest_index_3_2 = np.argmin(np.abs(E_values - 3.2))

plt.text(14.41, sigmaB_values[closest_index], f'{sigmaB_values[closest_index]:.3g}', fontsize=10, ha='right', va='top')
plt.text(3.2, sigmaB_values[closest_index_3_2], f'{sigmaB_values[closest_index_3_2]:.3g}', fontsize=10, ha='right', va='top')

plt.savefig('sigmaB_131Xe(abs).png') 
#plt.savefig('sigmaB_131Xe(abs)3.0eV.png') 
plt.show()