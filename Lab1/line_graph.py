import matplotlib.pyplot as plt

interval = [x for x in range(0, 10)]
groupA = [1.003, 0.973, 1.006, 0.993, 1.026, 1.016, 0.999, 0.95, 1.013, 0.961]
groupB = [0.977, 0.972, 1.03, 1.015, 1.005, 1.023, 0.999, 0.998, 1.025, 0.99]
groupC = [1.115, 1.055, 1.068, 1.076, 1.105, 1.119, 1.096, 1.118, 1.132, 1.103]
groupD = [0.991, 0.998, 1, 0.997, 1.043, 0.941, 1.057, 0.922, 1.026, 0.905]

constant = [1] * 10

plt.plot(interval, groupA, color='cyan')
plt.plot(interval, groupB, color='orange')
plt.plot(interval, groupC, color='green')
plt.plot(interval, groupD, color='purple')
plt.plot(interval, constant, color='black')

plt.xlabel('Interval')
plt.ylabel('Time in seconds')
plt.show()
