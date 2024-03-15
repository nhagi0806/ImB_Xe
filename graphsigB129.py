import math
import numpy as np
import const129
import pandas as pd
import ReImB
import matplotlib.pyplot as plt

E_values = np.linspace(2.5, 20, 1000)  

siggmaB_values = [ReImB.siggmaB129(E) for E in E_values]

plt.plot(E_values, siggmaB_values)
plt.xlabel('E (eV)')  
plt.ylabel('siggmaB(barn)')  
plt.title('siggmaB129')  
plt.grid(True)  

plt.yscale('log') 

plt.savefig('siggmaB_129Xe.png')  
plt.show()