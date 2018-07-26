#!/usr/bin/env python3

import pylab as pl
import numpy as np


def f(x):
    return x**4 - 2*x + 1


def f_1(x):
    return x**5 / 5 - x**2 + x


def integral(f, N, a, b):
    h = (b - a) / N
    result = 0.5 * f(a) + 0.5 * f(b)
    for k in range(1, N):
        result += f(a + k * h)

    result = h * result

    return result


area_exact = f_1(1) - f_1(0)
N = []
deltas = []
for n in range(1, 1000):
    N.append(n)
    area_trapezoidal = integral(f, n, 0, 1)
    delta = np.abs(area_trapezoidal - area_exact) / area_exact
    deltas.append(delta)

pl.plot(N, deltas)
pl.title("Error development of trapezoidal integration method")
pl.xlabel("Number of trapezoidal slices")
pl.ylabel("Error")
pl.yscale("log")
pl.show()
