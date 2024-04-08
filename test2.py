import ROOT
import numpy as np

def dsigHe(E):
    sigma_0 = 5333    # barn
    E_He = 25 * 10**-3   # eV
    return sigma_0 * (np.sqrt(E_He) / np.sqrt(E))
    #p0 = 854.0617248564827
    #return (p0 / np.sqrt(E)) 

def Polen(E):
    P_He = 0.655
    rho_He = 2.686 * 10**19 * 10**6  # m^-2
    d_He = 21.36*10**-2    # m
    return np.tanh(P_He * rho_He * d_He * dsigHe(E) / 10**28)

# エネルギー範囲
E_range = np.linspace(1, 50, 1000)

# dsigHeとPolenの値を計算
dsigHe_vals = [dsigHe(E) for E in E_range]
polen_vals = [Polen(E) for E in E_range]

# dsigHeのグラフ
graph_dsigHe = ROOT.TGraph(len(E_range), E_range, np.array(dsigHe_vals))
c1 = ROOT.TCanvas("c1", "dsigHe", 800, 600)
graph_dsigHe.SetTitle("dsigHe(E);Energy (eV);Cross Section (barn)")
graph_dsigHe.SetLineColor(ROOT.kRed)
graph_dsigHe.Draw("AL")
c1.Draw()
#c1.SaveAs("dsigHe_plot.png")

# Polenのグラフ
graph_polen = ROOT.TGraph(len(E_range), E_range, np.array(polen_vals))
c2 = ROOT.TCanvas("c2", "Polen", 800, 600)
graph_polen.SetTitle("Polen(E);Energy (eV);Polen(E)")
graph_polen.SetLineColor(ROOT.kBlue)
graph_polen.Draw("AL")
c2.Draw()
#c2.SaveAs("Polen_plot.png")