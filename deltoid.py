#!/usr/bin/env python3

import pylab
import numpy as np


theta = np.linspace(0, 2*np.pi, 1000)
x = 2 * np.cos(theta) + np.cos(2 * theta)
y = 2 * np.sin(theta) - np.sin(2 * theta)

pylab.title('deltoid')
pylab.xlabel('x')
pylab.ylabel('y')
pylab.plot(x, y)
pylab.show()
