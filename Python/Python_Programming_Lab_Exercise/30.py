# Write a program using matplotlib to plot line and bar graphs.

import matplotlib.pyplot as plt

x = [1, 2, 3]
y = [10, 20, 30]

# Line graph
plt.plot(x, y)
plt.title("Line Graph")
plt.show()

# Bar graph
plt.bar(x, y)
plt.title("Bar Graph")
plt.show()