import os
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
# from matplotlib import animation
from matplotlib.animation import FuncAnimation

array_size = np.random.randint(1000,10000)
print(f'Creating animation with array size: {array_size}')
x_init = np.random.random(array_size)
y_init = np.random.random(array_size)
nbins = 50
bins = [nbins, nbins]
colormap = 'viridis'#'inferno'


f, ax = plt.subplots()
hist = ax.hist2d(x_init, y_init, bins=bins, cmap=colormap)

ax.set_axis_off()

def init():
    
    hist = ax.hist2d(x_init, y_init, bins=bins, cmap=colormap)
    return hist

def animate(frame):
    '''Update figure using FuncAnimation'''
    ax.clear()
    ax.set_axis_off()
    x = np.random.random(array_size)
    y = np.random.random(array_size)
    hist = ax.hist2d(x,y, bins=bins,  cmap=colormap)
    return hist

if __name__ == "__main__":
    print("Let's go.")

    # call the animator.  blit=True means only re-draw the parts that have changed.
    anim = FuncAnimation(f, animate, init_func=init,
                                frames=100, interval=25, repeat=False)#, blit=True)

    plt.show()
    anim.save('hist_animation.mp4')

    
