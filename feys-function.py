#!/usr/bin/env python3

import pylab as pl
import numpy as np
from basic_units import radians


theta = np.linspace(0, 24*np.pi, 10000)
r = np.exp(np.cos(theta)) - \
    2 * np.cos(4 * theta) + \
    np.power(np.sin(theta / 12), 5)

x = []
y = []
for index, value in enumerate(theta):
    x.append(r[index] * np.cos(value))
    y.append(r[index] * np.sin(value))

pl.title(r"Fey's Function")
pl.plot(x, y, xunits=radians, yunits=radians)
pl.show()
