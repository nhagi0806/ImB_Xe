import ROOT
import numpy as np

def He_total(E):
    p0 = 854.0617248564827
    return (p0 / np.sqrt(E)) 

def Poln(E, p_He=0.665, rho_d_He=2.686*10**19*21.36):
    dSigma_He = He_total(E)
    return np.tanh(p_He * rho_d_He * dSigma_He/10**28)

def plot_with_pyroot():
    # グラフのデータを準備
    n_points = 1000
    E_range = np.linspace(1, 50, n_points)
    
    # Poln(E)のグラフ
    graph_poln = ROOT.TGraph(n_points)
    for i, E in enumerate(E_range):
        y = Poln(E)
        graph_poln.SetPoint(i, E, y)
    
    # He_total(E)のグラフ
    graph_he_total = ROOT.TGraph(n_points)
    for i, E in enumerate(E_range):
        y = He_total(E)
        graph_he_total.SetPoint(i, E, y)
    
    # Poln(E)グラフの設定と描画
    c1 = ROOT.TCanvas("c1", "Poln(E)", 800, 600)
    graph_poln.SetTitle("Poln(E) Plot;Energy (E);Poln(E)")
    graph_poln.SetLineColor(4)  # 青色
    graph_poln.SetLineWidth(2)
    graph_poln.Draw("AL")
    c1.Draw()
    c1.SaveAs("PolnE_plot.png")  # PDFファイルとして保存
    
    # He_total(E)グラフの設定と描画
    c2 = ROOT.TCanvas("c2", "He(E)", 800, 600)
    graph_he_total.SetTitle("He(E) Plot;Energy (E);He_total(E)")
    graph_he_total.SetLineColor(2)  # 赤色
    graph_he_total.SetLineWidth(2)
    graph_he_total.Draw("AL")
    c2.Draw()
    c2.SaveAs("HeTotalE_plot.png")  # PDFファイルとして保存

    input("Press Enter to continue...")  # ウィンドウを開いたままにする

# 実行
plot_with_pyroot()