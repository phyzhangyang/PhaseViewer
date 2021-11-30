#!/usr/bin/env python3
##############################################################
"""
    ___ _                          _
   / _ \ |__   __ _ ___  ___/\   /(_) _____      _____ _ __
  / /_)/ '_ \ / _` / __|/ _ \ \ / / |/ _ \ \ /\ / / _ \ '__|
 / ___/| | | | (_| \__ \  __/\ V /| |  __/\ V  V /  __/ |
 \/    |_| |_|\__,_|___/\___| \_/ |_|\___| \_/\_/ \___|_|

    A tool for visualizing cosmological phase transitions.
        
    Author:
    Web: https://github.com/phyzhangyang/PhaseViewer
                                                           """
##############################################################

## External modules.
import imageio
import os,sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm, rc
sys.path.append(os.path.join(os.path.split(os.path.realpath(__file__))[0], "src"))
## Internal modules.
import initialize
from potential_2d import Veff

try:
    latex = os.environ["MATPLOTLIB_LATEX"]
except KeyError:
    latex = False
if latex:
    rc('text', usetex=True)
    rc('font', **{'family': 'serif'})
    rc('font', **{'family': 'serif', 'size': 14})

scale = 1e-6
TC = 59.2297
h = np.linspace(-20, 100, 200)
s = np.linspace(-20, 100, 200)
hh, ss = np.meshgrid(h, s)

T = np.linspace(0, 100, 20)
#T = np.array([0, 10, 20, 30, 40, 50, 55, TC, 60, 65, 70, 80])

#xx, TT = np.meshgrid(x, T)
#VV = V(xx, TT)
#cp = ax.scatter(xx, scale * VV, c=TT, s=5, edgecolor='None', cmap=cm.get_cmap('rainbow', 15), alpha=0.8)


frames = []
for ii in range(len(T)):

  fig, ax = plt.subplots()
  Ti = T[ii]
  Vi = Veff([hh,ss], Ti)
  
  cp = ax.scatter(hh, ss, c=Vi, s=5, edgecolor='None', alpha=0.8)

#  ax.text(43, -0.1, r'$T_C=59.2$ GeV')

  plt.ticklabel_format(axis='y', style='sci', scilimits=(0, 3))
  plt.grid(True, linestyle=':')

#  ax.set_ylim(-1, 0.5)
#  ax.set_xlim(-20, 90)
  ax.set_ylabel(r'$V(\phi) \times 10^{-6}$ (GeV)${}^4$')
  ax.set_xlabel(r'$\phi$ (GeV)')

#  cb = fig.colorbar(cp)
#  cb.set_label(r"$T$ (GeV)")

  ax.set_title("T="+str(Ti))
#  plt.show()

  plt.savefig('temp.png', bbox_inches='tight')
  
  frames.append(imageio.imread('temp.png'))

gif_name = 'new.gif'
duration =0.5
imageio.mimsave(gif_name, frames, 'GIF', duration=duration)


