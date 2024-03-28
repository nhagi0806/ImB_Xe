import math
import numpy as np
import const129
import pandas as pd
import ReImB
import matplotlib.pyplot as plt

E_values = np.linspace(2.5, 20, 1000)  

sigmaA_values = [ReImB.sigmaA131(E) for E in E_values]

sigmaB_values = [ReImB.sigmaB131(E) for E in E_values]

plt.plot(E_values, sigmaA_values, label='sigmaA131')
plt.plot(E_values, sigmaB_values, label='sigmaB131')
plt.xlabel('E (eV)')
plt.ylabel('sigma (barn)')
plt.title('sigmaA131 and sigmaB131')
plt.grid(True)
plt.legend()  
  

closest_index = np.argmin(np.abs(E_values - 14.41))

plt.text(14.41 + 0.1, sigmaA_values[closest_index], f'{sigmaA_values[closest_index]:.3g}', fontsize=10, ha='left', va='bottom')
plt.text(14.41 + 0.1, sigmaB_values[closest_index], f'{sigmaB_values[closest_index]:.3g}', fontsize=10, ha='left', va='bottom')

plt.savefig('sigmaAB_131Xe.png')  
plt.show()