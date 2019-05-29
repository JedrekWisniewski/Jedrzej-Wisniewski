import numpy as np
import matplotlib as m
import matplotlib.pylab as plt

def wyswietlacz(macierz):
    colors = ['white','red','red','red','red','blue','gray','gray','gray','gray']
    cmap_name = 'my_colormap'
    cm = m.colors.LinearSegmentedColormap.from_list(cmap_name, colors)

    matrix = np.load(macierz)
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
    minorLocator = m.ticker.IndexLocator(base=1, offset=1)
    ax.yaxis.set_minor_locator(minorLocator)
    ax.xaxis.set_minor_locator(minorLocator)
    ax.grid(which='minor', color='black')
    ax.tick_params(axis='x', bottom=True, top=True, labelbottom=True, labeltop=True)
    ax.tick_params(axis='y', right=True, left=True, labelright=True, labelleft=True)
    
    x = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    plt.imshow(matrix,cmap=cm,vmin=-5,vmax=4)
    labels = range(0,10)
    plt.yticks(labels,[1,2,3,4,5,6,7,8,9,10])
    plt.xticks(labels,[x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8],x[9]])
    plt.show()

wyswietlacz("Gracz1.npy")
