#!/usr/bin/env python3

import pylab as pl
import numpy as np


x_start = 0.5
N = 1000
R = np.arange(1.0, 4.0, 0.01)

pl.title("Feigenbaum Plot")

for r in R:
    x = x_start
    for _ in range(N - 1):
        x2 = r * x * (1 - x)
        x = x2
    x_result = [x]
    for _ in range(int(N/10) - 1):
        x2 = r * x * (1 - x)
        x_result.append(x)
        x = x2
    horizontal = np.full((int(N/10), 1), r)
    pl.scatter(horizontal, x_result, s=1.0, marker=",", color="black")

pl.show()
