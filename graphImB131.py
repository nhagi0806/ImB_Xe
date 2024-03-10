import math
import numpy as np
import const131
import pandas as pd
import ReImB
import matplotlib.pyplot as plt

# グラフを描画する範囲を設定
E_values = np.linspace(0, 50, 100000)  # 0から10までの間を100点で分割して計算

# 関数を適用し、結果を取得
ImB_values = [ReImB.ImB_131Xe(E) for E in E_values]

# グラフを描画
plt.plot(E_values, ImB_values)
plt.xlabel('E')  # x軸のラベル
plt.ylabel('ImB_131Xe(E)')  # y軸のラベル
plt.title('ImB_131Xe(E) vs E')  # グラフのタイトル
plt.grid(True)  # グリッドを表示
plt.show()  # グラフを表示