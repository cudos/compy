#!/usr/bin/env python3

from pylab import plot, show
from numpy import linspace, sin

x = linspace(0, 10, 1000)
y = sin(x)
plot(x, y)
show()
