#!/usr/bin/env python3

import pylab as pl
import numpy as np

data = np.loadtxt("stars.txt", float)
x = data[:, 0]
y = data[:, 1]

pl.scatter(x, y, marker=".")
pl.title("Herzsprung Russel Diagramm")
pl.xlabel("Temperature")
pl.ylabel("Magnitude")
pl.show()
