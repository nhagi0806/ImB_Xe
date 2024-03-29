import math
import numpy as np
import const129
import pandas as pd
import ReImB
import matplotlib.pyplot as plt

E_values = np.linspace(2.5, 20, 1000)  
#E_values = np.linspace(0.001, 0.2, 1000)  #0.1eVと0.02eVの計算

sigmaB_values = [ReImB.sigmaB129(E) for E in E_values]

plt.plot(E_values, sigmaB_values)
plt.xlabel('E (eV)')  
plt.ylabel('sigmaB(barn)')  
plt.title('sigmaB129')  
plt.grid(True)  

plt.yscale('log') 

closest_index = np.argmin(np.abs(E_values - 9.57))
#closest_index_01 = np.argmin(np.abs(E_values - 0.1))
#closest_index_02 = np.argmin(np.abs(E_values - 0.02))

plt.text(9.57 + 0.1, sigmaB_values[closest_index], f'{sigmaB_values[closest_index]:.3g}', fontsize=10, ha='left', va='bottom')
#plt.text(0.1, sigmaB_values[closest_index_01], f'{sigmaB_values[closest_index_01]:.3g}', fontsize=10, ha='left', va='bottom')     #0.1eVと0.02eVの計算
#plt.text(0.02, sigmaB_values[closest_index_02], f'{sigmaB_values[closest_index_02]:.3g}', fontsize=10, ha='left', va='bottom')    #0.1eVと0.02eVの計算

plt.savefig('sigmaB_129Xe.png')
#plt.savefig('sigmaB_129Xe(0.02eV&0.1eV).png')    #0.1eVと0.02eVの計算
plt.show()