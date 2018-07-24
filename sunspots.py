#!/usr/bin/env python3

import numpy as np
import pylab


np.set_printoptions(threshold=np.nan)

data = np.loadtxt('sunspots.txt')
N = 1000

month = data[:N, 0]
sunspots = data[:N, 1]

# Calculate running average
window = 5
moving_averages = []
for i in range(N):
    avg_values = sunspots[i - window:i + window + 1]
    moving_averages.append(np.average(avg_values))

# Plot
pylab.xlabel('month')
pylab.title('Number of Sunspots since 1749')
pylab.ylabel('sunspots')
pylab.plot(month, sunspots, 'k.', label='sunspots')
pylab.plot(month, moving_averages, linewidth=2, label='moving average (10 month)')
pylab.legend(loc='uppper right')
pylab.show()
