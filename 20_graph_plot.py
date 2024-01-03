# Project 20
# Graph Plotter

# pip install matplotlib
import matplotlib.pyplot as plt


# For 1 Line
x = [1, 2, 5]
y = [2, 3, 4]

plt.plot(x, y, color='green', linestyle='dashed', marker='o',
         markerfacecolor='blue', markersize=12)

plt.xlim(0,6)
plt.ylim(0,6)

plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.title('Demo Graph')

plt.show()


"""
# For 2 Lines

x1 = [1, 2, 5]
y1 = [2, 3, 4]
plt.plot(x1, y1, label = 'Line-1')

x2 = [2, 4, 4]
y2 = [1, 2, 5]
plt.plot(x2, y2, label = 'Line-2')

plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.title('Demo Graph - Two Lines')
plt.legend()

plt.show()
"""

# For Bar Graph
x = [1, 2, 4, 5, 9]
y = [2, 3, 4, 7, 6]

tick_label = ['i', 'ii', 'iii', 'iv', 'v']

plt.bar(x, y, tick_label=tick_label, width=0.8, color=['blue','orange'])

plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.title('Bar Graph')

plt.show()
