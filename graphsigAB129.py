import math
import numpy as np
import const129
import pandas as pd
import ReImB
import matplotlib.pyplot as plt

E_values = np.linspace(2.5, 20, 1000)  

sigmaA_values = [ReImB.sigmaA129(E) for E in E_values]

sigmaB_values = [ReImB.sigmaB129(E) for E in E_values]

plt.plot(E_values, sigmaA_values, label='sigmaA129')
plt.plot(E_values, sigmaB_values, label='sigmaB129')
plt.xlabel('E (eV)')
plt.ylabel('sigma (barn)')
plt.title('sigmaA129 and sigmaB129')
plt.grid(True)
plt.legend()  

plt.yscale('log')  

closest_index = np.argmin(np.abs(E_values - 9.57))

plt.text(9.57 + 0.1, sigmaA_values[closest_index], f'{sigmaA_values[closest_index]:.3g}', fontsize=10, ha='left', va='bottom')
plt.text(9.57 + 0.1, sigmaB_values[closest_index], f'{sigmaB_values[closest_index]:.3g}', fontsize=10, ha='left', va='bottom')

plt.savefig('sigmaAB_129Xe.png')  
plt.show()