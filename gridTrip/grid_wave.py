import os
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
# from matplotlib import animation
from matplotlib.animation import FuncAnimation

class gridTrip(object):

    def __init__(self, nbins=50, cmap='viridis', frames=100, interval=25, savefig=True):
        """
        Class to generate an animated 2d histogram of random data
        
        parameters:
            nbins: int or list, default 50; # of bins to use in histogram.
                    if list-like, the values should correspond to [xbins, ybins]
            cmap: str, default viridis; matplotlib-style colormap to use
            frames: int, default 100; # of frames for the animation to loop throug
            interval: int, default 25; delay (in milliseconds) between frames. Passed to FuncAnimate
            savefig: bool, default True; if True, save animationa s a gif stored in output directory
        """
        # Generating random init values
        self.array_size = np.random.randint(1000,10000)
        print(f'Creating animation with array size: {self.array_size}')
        self.x_init = np.random.random(self.array_size)
        self.y_init = np.random.random(self.array_size)

        # Histogram params - can be toggled by user
        self.bins = nbins
        self.colormap = cmap
        
        # Creating figure -- no ticks/border
        self.f, self.ax = plt.subplots(figsize=(8,8))
        self.ax.set_axis_off()

        # Creating animation
        anim = FuncAnimation(self.f, self.animate, init_func=self.init,
                                    frames=frames, interval=interval, repeat=False)
        plt.show()
        
        # Save to output dir
        if savefig:
            figpath = os.path.join('output', f'hist2d_{self.colormap}_{self.array_size}.gif')
            print(f"saving figure to path: {figpath}")
            anim.save(figpath)


    def init(self):
        
        hist = self.ax.hist2d(self.x_init, self.y_init, bins=self.bins, cmap=self.colormap)
        return hist

    def animate(self, frame):
        '''Update figure using FuncAnimation'''
        self.ax.clear()
        self.ax.set_axis_off()
        x = np.random.random(self.array_size)
        y = np.random.random(self.array_size)
        hist = self.ax.hist2d(x,y, bins=self.bins,  cmap=self.colormap)
        return hist

if __name__ == "__main__":
    print("Let's go.")

    gt = gridTrip(nbins=25, cmap='plasma')


    

    
