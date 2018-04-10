#!/usr/bin/env python
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

groupA = [1.003, 0.973, 1.006, 0.993, 1.026, 1.016, 0.999, 0.95, 1.013, 0.961]
groupB = [0.977, 0.972, 1.03, 1.015, 1.005, 1.023, 0.999, 0.998, 1.025, 0.99, 0.984, 1.018, 0.985, 0.981, 1.007, 0.945, 1.008, 0.983]
groupC = [1.115, 1.055, 1.068, 1.076, 1.105, 1.119, 1.096, 1.118, 1.132, 1.103]
groupD = [0.991, 0.998, 1, 0.997, 1.043, 0.941, 1.057, 0.922, 1.026, 0.905]

classA = [1.31, 1.47, 1.26, 1.56, 1.28, 1.46, 1.2, 1.38, 1.25, 1.21, 1.338]
classB = [1.2, 1.25, 1.3, 1.35, 1.4, 1.4, 1.5, 1.55, 1.6]

datasetA = {"groupA":groupA, "groupB":groupB, "groupC":groupC, "groupD":groupD}
datasetB = {"classA":classA, "classB":classB}

colorsA = iter(["red", "orange", "yellow", "cyan"])
colorsB = iter(["cyan", "red"])

bins = 10

def main():
    plt.xlabel('Time in seconds')
    plt.ylabel('Probability')

    for k,v in datasetA.items():
        plt.hist(v, bins, facecolor=colorsA.__next__(), alpha=0.4, label=k)

    generateLegend()
    plt.show()

    for k,v in datasetB.items():
        plt.hist(v, bins, facecolor=colorsB.__next__(), alpha=0.4, label=k)

    generateLegend()
    plt.show()

def generateLegend():
    legend = plt.legend(loc='upper center', shadow=True)

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
