import numpy as np
import matplotlib.pyplot as plt
import math
import const131
import const129
import constHe
import pandas as pd
import ReImB

E_values = np.linspace(1, 20, 100000)  
#E_values = np.linspace(1, 4, 1000)  #E=3.0eVを見る

epsilon_values = ReImB.epsilon131(E_values)

plt.plot(E_values, epsilon_values)
plt.xlabel('E')
plt.ylabel('epsilon131(E)')
plt.title('epsilon131(E) vs E')
plt.grid(True)

closest_index = np.argmin(np.abs(E_values - 14.41))
closest_index = np.argmin(np.abs(E_values - 3.20))

plt.text(14.41, ReImB.epsilon131(14.41), f'y={ReImB.epsilon131(14.41):.3g}', ha='right', va='bottom')
plt.text(3.20, ReImB.epsilon131(3.20), f'y={ReImB.epsilon131(3.20):.3g}', ha='right', va='bottom')
plt.savefig('asym_131Xe.png')  
#plt.savefig('asym100_131Xe.png')  #もし偏極率が１００なら
#plt.savefig('asym_131Xe3.0.png')  #3.0eVにズーム
plt.show()  

