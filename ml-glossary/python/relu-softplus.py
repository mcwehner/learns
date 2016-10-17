# Source: https://en.wikipedia.org/wiki/File:Rectifier_and_softplus_functions.svg

# coding=UTF8
#
# python code to plot nonlinearity functions
# written 2015 by Dan Stowell, dedicated to the public domain

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 6})

nlfuns = {
        'Rectifier':     ('b', '', lambda x: np.maximum(0, x)),
        'Softplus':      ('g', '', lambda x: np.log(1 + np.exp( 1 * x))/ 1),
#       'Softplus c=10': ('r', '', lambda x: np.log(1 + np.exp(10 * x))/10),
#       'Exponential':   ('c', '', lambda x: np.exp(x)),
}

evalpoints = np.linspace(-4, 4, 51)

params = {
   'axes.labelsize': 10,
   'text.fontsize': 10,
   'legend.fontsize': 10,
   'xtick.labelsize': 8,
   'ytick.labelsize': 8,
   'text.usetex': False,
   'figure.figsize': [5.5, 4],
   'lines.markersize': 4,
}
plt.rcParams.update(params)


plt.figure(frameon=False)
plt.axes(frameon=0)
plt.axvline(0, color=[0.6]*3)
plt.axhline(0, color=[0.6]*3)
for nlname, (color, marker, nlfun) in nlfuns.items():
        plt.plot(evalpoints, map(nlfun, evalpoints), hold=True, label=nlname, color=color, marker=marker)
plt.title('Nonlinearities')
plt.xlim(-4, 4)
plt.ylim(-0.1, 4.5)
plt.legend(loc='upper left', frameon=False)
plt.xlabel('x')
plt.ylabel(u'σ(x)')
plt.savefig('Rectifier_and_softplus_functions.svg')
plt.close()
