import const129
import const131
import test2
import numpy as np
import ReImB
import ROOT
import time

def epsilon131pol(E):
    k = 0.6947*np.sqrt(E*10**3)*10**10
    return test2.Poln(E)*np.tanh(4.2*10**(-4)*const131.num_131*const131.d_cell*(4*np.pi/k)*ReImB.ImB_131Xe(E))

def epsilon129pol(E):
    k = 0.6947*np.sqrt(E*10**3)*10**10
    return test2.Poln(E)*np.tanh(1.9*10**(-2)*const129.num_129*const129.d_cell*(4*np.pi/k)*ReImB.ImB_129Xe(E))

# エネルギー範囲の定義
E_range = np.linspace(0.01, 20, 1000)  # 0.01 eVから20 eVまで

# epsilon131polとepsilon129polの計算
epsilon131_values = np.array([epsilon131pol(E) for E in E_range])
epsilon129_values = np.array([epsilon129pol(E) for E in E_range])

# epsilon131polのグラフを作成
graph_epsilon131 = ROOT.TGraph(len(E_range), E_range, epsilon131_values)
c1_name = f"c1_{timestamp}"  # キャンバス名にタイムスタンプを追加
c1 = ROOT.TCanvas(c1_name, "epsilon131pol", 800, 600)
graph_epsilon131.Draw("AL")
# 14.41 eVでのepsilon131polの値を表示
epsilon131_at_14_41 = epsilon131pol(14.41)
latex = ROOT.TLatex(14.41, epsilon131_at_14_41, f"({14.41}, {epsilon131_at_14_41:.2f})")
latex.Draw()

c1.SaveAs("epsilon131pol.png")

# epsilon129polのグラフを作成
graph_epsilon129 = ROOT.TGraph(len(E_range), E_range, epsilon129_values)
c2_name = f"c2_{timestamp}"  # キャンバス名にタイムスタンプを追加
c2 = ROOT.TCanvas(c2_name, "epsilon129pol", 800, 600)
graph_epsilon129.Draw("AL")
# 9.57 eVでのepsilon129polの値を表示
epsilon129_at_9_57 = epsilon129pol(9.57)
latex = ROOT.TLatex(9.57, epsilon129_at_9_57, f"({9.57}, {epsilon129_at_9_57:.2f})")
latex.Draw()

c2.SaveAs("epsilon129pol.png")

