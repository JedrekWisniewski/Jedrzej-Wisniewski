import numpy as np
import matplotlib as m
import matplotlib.pylab as plt

cdict = {
    'blue' : (0),
    'red' : (-1,-2,-3,-4),
    'gray' : (1,2,3,4)}

colors = [(0,0,1), (0,1,0), (1,0,0)]
cmap_name = 'my_colormap'
cm = m.colors.LinearSegmentedColormap.from_list(cmap_name, colors)

matrix = np.load('Gracz1.npy')
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.set_aspect('equal')
plt.imshow(matrix,cmap=cm)
plt.colorbar()
plt.show()

