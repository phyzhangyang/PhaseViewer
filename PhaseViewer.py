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

def create_gif(source, name, duration):
	"""
     生成gif的函数，原始图片仅支持png
     source: 为png图片列表（排好序）
     name ：生成的文件名称
     duration: 每张图片之间的时间间隔
	"""
	frames = []     # 读入缓冲区
	for img in source:
		frames.append(imageio.imread(img))
	imageio.mimsave(name, frames, 'GIF', duration=duration)
	print("处理完成")
try:
    latex = os.environ["MATPLOTLIB_LATEX"]
except KeyError:
    latex = False
if latex:
    rc('text', usetex=True)
    rc('font', **{'family': 'serif'})
    rc('font', **{'family': 'serif', 'size': 14})


def V(x, T):
    return -100*x**2 - 10.*x**3 + 0.1*x**4 + 0.1*x**2 * T**2


scale = 1e-6
TC = 59.2297
x = np.linspace(-20, 100, 600)
T = np.array([0, 20, 30, 40, 50, TC, 65, 70, 80])

#xx, TT = np.meshgrid(x, T)
#VV = V(xx, TT)
#cp = ax.scatter(xx, scale * VV, c=TT, s=5, edgecolor='None', cmap=cm.get_cmap('rainbow', 15), alpha=0.8)

for ii in range(len(T)):

  fig, ax = plt.subplots()
  Ti = T[ii]
  Vi = V(x, Ti)
  cp = ax.scatter(x, scale * Vi, c='r', s=5, edgecolor='None', alpha=0.8)

#  ax.text(43, -0.1, r'$T_C=59.2$ GeV')

  plt.ticklabel_format(axis='y', style='sci', scilimits=(0, 3))
  plt.grid(True, linestyle=':')

  ax.set_ylim(-1, 0.5)
  ax.set_xlim(-20, 90)
  ax.set_ylabel(r'$V(\phi) \times 10^{-6}$ (GeV)${}^4$')
  ax.set_xlabel(r'$\phi$ (GeV)')

#  cb = fig.colorbar(cp)
#  cb.set_label(r"$T$ (GeV)")

#  plt.show()

  plt.savefig(str(ii)+'.png', bbox_inches='tight')
def main():
     image_list=['1.png','2.png','3.png','4.png','5.png','6.png','7.png','8.png']
     gif_name = 'new.gif'
     duration =0.1
     create_gif(image_list,gif_name,duration)
main()
