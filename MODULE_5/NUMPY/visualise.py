import matplotlib.pyplot as plt
import numpy as np

x = [1,2,3,4,5]
y = [5,4,3,2,1]

data1 = np.array(x)

# plt.plot(x,y)
# plt.scatter(x,y)
# plt.bar(x,y)
# plt.boxplot(data1)

plt.pie(y, labels=x, autopct='%1.1f%%')


# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')
plt.title('PIE PLOT')

plt.show()