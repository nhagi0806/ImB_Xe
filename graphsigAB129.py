import math
import numpy as np
import const129
import pandas as pd
import ReImB
import matplotlib.pyplot as plt

E_values = np.linspace(2.5, 20, 1000)  

siggmaA_values = [ReImB.siggmaA129(E) for E in E_values]

siggmaB_values = [ReImB.siggmaB129(E) for E in E_values]

plt.plot(E_values, siggmaA_values, label='siggmaA129')
plt.plot(E_values, siggmaB_values, label='siggmaB129')
plt.xlabel('E (eV)')
plt.ylabel('siggma (barn)')
plt.title('siggmaA129 and siggmaB129')
plt.grid(True)
plt.legend()  

plt.yscale('log')  

closest_index = np.argmin(np.abs(E_values - 9.57))

plt.text(9.57 + 0.1, siggmaA_values[closest_index], f'{siggmaA_values[closest_index]:.3g}', fontsize=10, ha='left', va='bottom')
plt.text(9.57 + 0.1, siggmaB_values[closest_index], f'{siggmaB_values[closest_index]:.3g}', fontsize=10, ha='left', va='bottom')

plt.savefig('siggmaAB_129Xe.png')  
plt.show()