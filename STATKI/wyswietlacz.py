import numpy as np
import matplotlib as m
import matplotlib.pylab as plt

colors = ['red','red','red','red','blue','gray','gray','gray','gray']
cmap_name = 'my_colormap'
cm = m.colors.LinearSegmentedColormap.from_list(cmap_name, colors)

matrix = np.load('Gracz1.npy')
fig = plt.figure(facecolor='black')
ax = fig.add_subplot(1,1,1)
ax.set_aspect('equal')
ax.spines['bottom'].set_color('white')
ax.spines['top'].set_color('white')
ax.spines['right'].set_color('white')
ax.spines['left'].set_color('white')
ax.xaxis.label.set_color('white')
ax.yaxis.label.set_color('white')
ax.tick_params(axis='x', colors='white')
ax.tick_params(axis='y', colors='white')
plt.imshow(matrix,cmap=cm,vmin=-4,vmax=4)
plt.colorbar()
plt.grid(True)
plt.show()
