import matplotlib.pyplot as plt

interval = [x for x in range(0, 12)]

ten_swings = [1.416, 1.591, 1.416, 1.585, 1.426, 1.435, 1.602, 1.558 ,1.609 ,1.581 ,1.59 ,1.498]

twenty_swings = [1.568 ,1.5205 ,1.5865 ,1.574 ,1.5815 ,1.586, 1.5905, 1.5765, 1.598, 1.509, 1.5905, 1.5775]

forty_swings = [1.584, 1.585, 1.5815, 1.5865, 1.58575, 1.58925,
1.584, 1.58475, 1.5805, 1.5865, 1.58775, 1.58925]

constant = [1.58] * 12

colors = iter(["indianred", "darkorange", "gold"])

plt.plot(interval, ten_swings, color=colors.__next__())
plt.plot(interval, twenty_swings, color=colors.__next__())
plt.plot(interval, forty_swings, color=colors.__next__())
plt.plot(interval, constant, color='black')

plt.xlabel('Interval')
plt.ylabel('Time in seconds')
plt.grid()
plt.show()
