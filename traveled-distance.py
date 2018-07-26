#!/usr/bin/env python3

import numpy as np
import pylab as pl


data = np.loadtxt("velocities.txt")
t = data[:, 0]
v = data[:, 1]
x = []
area = 0
for k in range(0, len(data) - 1):
    area += (v[k] + v[k + 1]) * (t[k + 1] - t[k])
    x.append(0.5 * area)

pl.title("Traveled distance")
pl.xlabel("t / s")
pl.ylabel("v / m/s and x / m")
pl.plot(t, v, label="velocity")
pl.plot(t[:-1], x, label="traveled distance")
pl.legend()
pl.grid()
pl.show()
