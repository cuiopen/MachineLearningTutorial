#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
# Created by C.L.Wang
import numpy as np

# fig, axs = plt.subplots(1, 1)
#
# x = np.linspace(0, 1, 100)
# X, Y = np.meshgrid(x, x)
# Z = np.sin(X) * np.sin(Y)
#
# levels = np.linspace(-1, 1, 40)
#
# zdata = np.sin(8 * X) * np.sin(8 * Y)
#
# # cs = axs[0].contourf(X, Y, zdata, levels=levels)
# # fig.colorbar(cs, ax=axs[0], format="%.2f")
#
# cs = axs.contourf(X, Y, zdata, levels=[-1, 0, 1])
# fig.colorbar(cs, ax=axs)
#
# plt.show()
from wilson_score.wilson_score import wilson_score

value = np.linspace(0.01, 100, 1000)
u, v = np.meshgrid(value, value)

fig, ax = plt.subplots(1, 2)
levels = np.linspace(0, 1, 10)

cs = ax[0].contourf(u, v, wilson_score(u, u + v), levels=levels)
cb1 = fig.colorbar(cs, ax=ax[0], format="%.2f")

cs = ax[1].contourf(u, v, wilson_score(u, u + v, 6.), levels=levels)
cb2 = fig.colorbar(cs, ax=ax[1], format="%.2f")

ax[0].set_xlabel(u'pos')
ax[0].set_ylabel(u'neg')
cb1.set_label(u'wilson(z=2)')

ax[1].set_xlabel(u'pos')
ax[1].set_ylabel(u'neg')
cb2.set_label(u'wilson(z=6)')

plt.show()
