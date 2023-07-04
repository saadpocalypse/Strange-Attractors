import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as mcolors

def xEquation(prevValueX, prevValueY):
    newValue = d * np.sin(prevValueX * a) - np.sin(prevValueY * b)
    return [newValue]

def yEquation(prevValueX, prevValueY):
    newValue = c * np.cos(prevValueX * a) + np.cos(prevValueY * b)
    return [newValue]

a = 1.40 
b = 1.56 
c = 1.40 
d = -6.56

plt.figure(facecolor='black')
plt.rcParams['axes.facecolor'] = 'black'
plt.xticks([])
plt.yticks([])

x = [0]
y = [0]
plt.plot(x, y, 'bo', markersize=0.1)

color_start = '#d18d9e'
color_end = '#9a8dd1'

cmap = mcolors.LinearSegmentedColormap.from_list('custom', [color_start, color_end])

for i in range(100000):
    tempX = x
    tempY = y
    x = xEquation(tempX[0], tempY[0])
    y = yEquation(tempX[0], tempY[0])
    color_value = i / 100000
    color = cmap(color_value)
    plt.plot(x, y, markersize=0.1, marker='o', color=color)

plt.grid(False)
plt.show()
