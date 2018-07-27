#!/usr/bin/env python3

import pylab as pl
import numpy as np


def f(x):
    return x**4 - 2*x + 1


def df(x):
    return x**5 / 5 - x**2 + x


def integrate_simpson(f, a, b, N):
    result = f(a) + f(b)
    h = (b - a) / N
    for k in range(1, N, 2):
        result += 4 * f(a + k * h)

    for k in range(2, N, 2):
        result += 2 * f(a + k * h)

    result = 1/3 * h * result

    return result


def integrate_exact(a, b):
    return df(b) - df(a)


exact_result = integrate_exact(0, 2)
num_of_slices = []
integrals = []
errors = []
for n in range(2, 1000, 2):
    num_of_slices.append(n)
    integral = integrate_simpson(f, 0, 2, n)
    integrals.append(integral)
    error = np.abs(integral - exact_result) / exact_result
    errors.append(error)


pl.subplot(2, 1, 1)
pl.title("Integrate $x^4 - 2*x + 1$ with Simpson's rule")
pl.ylabel("Integral value")
pl.plot(num_of_slices, integrals, "k.")

pl.subplot(2, 1, 2)
pl.yscale("log")
pl.xlabel("Number of slices")
pl.ylabel("Error (log scale)")
pl.plot(num_of_slices, errors)
pl.show()
