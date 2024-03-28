import numpy as np
import matplotlib.pyplot as plt
import math
import const131
import const129
import constHe
import pandas as pd
import ReImB

E_values = np.linspace(1, 20, 100000)  

epsilon_values = ReImB.epsilon129(E_values)
#epsilon_values = ReImB.epsilon129_1atm(E_values)  #1atmセルでのグラフ

plt.plot(E_values, epsilon_values)
plt.xlabel('E')
plt.ylabel('epsilon129(E)')
plt.title('epsilon129(E) vs E')
plt.grid(True)

closest_index = np.argmin(np.abs(E_values - 9.57))

plt.text(9.57, ReImB.epsilon129(9.57), f'y={ReImB.epsilon129(9.57):.3g}', ha='right', va='bottom')
#plt.text(9.57, ReImB.epsilon129_1atm(9.57), f'y={ReImB.epsilon129_1atm(9.57):.3g}', ha='right', va='bottom')   #1atmセルでのグラフ
plt.savefig('asym_129Xe.png')  
#plt.savefig('asym_129Xe_1atm.png')  #1atmセルでのグラフ
plt.show()  