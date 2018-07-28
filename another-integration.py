#!/usr/bin/env python3

import pylab as pl
import numpy as np


N = 100


def f(x):
    return np.exp(-x**2)


def integrate_simpson(f, a, b):
    h = (b - a) / N
    result = f(a) + f(b)
    for k in range(1, N, 2):
        result += 4 * f(a + k * h)

    for k in range(1, N, 2):
        result += 2* f(a + k * h)

    result = 1/3 * h * result

    return result


x_values = []
I_values = []
for x in np.arange(0, 3.1, 0.1):
    x_values.append(x)
    integral = integrate_simpson(f, 0, x)
    I_values.append(integral)

pl.title("Integrate E(x) = e^(-k^2) over [0, x] with Simpson's rule")
pl.xlabel("x")
pl.ylabel("E(x)")
pl.plot(x_values, I_values)
pl.show()
