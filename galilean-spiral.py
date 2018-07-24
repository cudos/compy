#!/usr/bin/env python3

import pylab as pl
import numpy as np
from basic_units import radians


theta = np.linspace(0, 10*np.pi, 1000)
r = np.power(theta, 2)

x = []
y = []
for index, value in enumerate(theta):
    x.append(r[index] * np.cos(value))
    y.append(r[index] * np.sin(value))

pl.title(r'Galilean Spiral r = $\theta^2$')
pl.plot(x, y, xunits=radians, yunits=radians)
pl.show()
