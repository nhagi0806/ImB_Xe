import math
import numpy as np
import const129
import pandas as pd
import ReImB
import matplotlib.pyplot as plt

E_values = np.linspace(1, 20, 1000) 

siggmaB_values = [ReImB.siggmaB131(E) for E in E_values]

plt.plot(E_values, siggmaB_values)
plt.xlabel('E (eV)')  
plt.ylabel('siggmaB(barn)')  
plt.title('siggmaB131')  
plt.grid(True)  

closest_index = np.argmin(np.abs(E_values - 14.41))

plt.text(14.41 + 0.1, siggmaB_values[closest_index], f'{siggmaB_values[closest_index]:.3g}', fontsize=10, ha='left', va='bottom')

plt.savefig('siggmaB_131Xe.png')  
plt.show()