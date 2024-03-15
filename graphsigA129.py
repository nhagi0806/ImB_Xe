import math
import numpy as np
import const129
import pandas as pd
import ReImB
import matplotlib.pyplot as plt

E_values = np.linspace(2.5, 20, 1000)  

siggmaA_values = [ReImB.siggmaA129(E) for E in E_values]

plt.plot(E_values, siggmaA_values)
plt.xlabel('E (eV)')  
plt.ylabel('siggmaA(barn)')  
plt.title('siggmaA129')  
plt.grid(True)  

plt.yscale('log')  

plt.savefig('siggmaA_129Xe.png')  
plt.show()