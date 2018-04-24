#!/usr/bin/env python
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

from scipy.stats import gaussian_kde

ten_swings = [1.416, 1.591, 1.416, 1.585, 1.426, 1.435, 1.602, 1.558 ,1.609 ,1.581 ,1.59 ,1.498]

twenty_swings = [1.568 ,1.5205 ,1.5865 ,1.574 ,1.5815 ,1.586, 1.5905, 1.5765, 1.598, 1.509, 1.5905, 1.5775]

forty_swings = [1.584, 1.585, 1.5815, 1.5865, 1.58575, 1.58925,
1.584, 1.58475, 1.5805, 1.5865, 1.58775, 1.58925]

dataset = {"10 swings":ten_swings, "20 swings":twenty_swings, "40 swings":forty_swings}

colors = iter(["indianred", "darkorange", "gold"])

bins = 3

def main():
    plt.xlabel('Time in seconds')
    plt.ylabel('Density')

    for k,v in dataset.items():
        density = gaussian_kde(v)
        xs = np.linspace(1.3,1.8,42)
        density.covariance_factor = lambda : .2
        density._compute_covariance()
        plt.plot(xs, density(xs), color=colors.__next__(), label=k)

    generateLegend()
    plt.grid()
    plt.show()

def generateLegend():
    legend = plt.legend(loc='upper left', shadow=True)

    frame = legend.get_frame()
    frame.set_facecolor('0.90')

    # Set the fontsize
    for label in legend.get_texts():
        label.set_fontsize('large')

    for label in legend.get_lines():
        label.set_linewidth(1.5)
    return

if __name__ == "__main__":
    main()
