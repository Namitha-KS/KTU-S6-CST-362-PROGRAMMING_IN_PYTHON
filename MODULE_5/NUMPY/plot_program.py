'''plot two or more lines on a same plot with suitable
legends, labels and title.'''

import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [2.7,16,44,15,6]
z = [13,24,35,46,57]

plt.plot(x, y, label = 'Line 1')
plt.plot(y, z, label = 'Line 2')

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('TWO LINES PLOT')

plt.legend()
plt.show()