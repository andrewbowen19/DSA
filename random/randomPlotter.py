# Plot some randomness!
#dsa/random/random.py

'''Script to generate plots of random datasets'''

import os
import numpy as np
import matplotlib.pyplot as plt
import uuid


class randomPlotter(object):

    def __init__(self):
        self.array_size = np.random.randint(0,1000)
        print(f"Your random number is {self.array_size}")

    def hist2d(self, colormap='Reds', savefig=False):
        '''
        Creates 2D histogram
        
        parameters:
            colormap : str; matplotlib.pyplot colormap name
            savefig : boolean (default false); if True, figure is saved to plots/hist2d directory
        '''
        x = np.arange(0, self.array_size, 1)
        y = np.random.random(x.size)

        f, ax = plt.subplots()
        ax.hist2d(x, y, cmap = colormap, bins=[25,25])
        ax.set_xticks([])
        ax.set_yticks([])
        
#        Saving the figure
        if savefig:
            file_path = os.path.join(".", "plots", "hist2d", f"hist2d_random_{colormap}_{self.array_size}.pdf")
            f.savefig(file_path)
#        plt.close()
        
    def plotCircles(self, colormap="inferno", set_title=False, savefig=False):
        '''
        Creates scatter plot of randomly sized circles
        '''
#        Generating x, y, size & color arrays
        x = np.random.random(self.array_size)
        y = np.random.random(self.array_size)
        s = np.random.randint(0,10, self.array_size)
        c = np.random.random(self.array_size)
        
        f, ax = plt.subplots()
        ax.scatter(x,y,s, c=c, cmap=colormap)
        ax.set_xticks([])
        ax.set_yticks([])
        
#        Setting figure title/saving figure if desired
        title_hash = ''
        if set_title:
            title_hash = uuid.uuid4().hex
            ax.set_title(title_hash)
            
        if savefig:
            file_path = os.path.join(".", "plots", "scatter", f"scatter_random_{colormap}_{self.array_size}.pdf")
            f.savefig(file_path)

    def sine(self, x):
        '''returns random sine values for an input array x'''
        a = np.random.uniform(-100,100)
        b = np.random.uniform(-100,100)
        c = np.random.uniform(-100,100)
        d = np.random.uniform(-100,100)
        print(f'Coefficients: a: {a} | b: {b} | c: {c} | d:{d}')
        y = a * np.sin((b * x) + c) + d
        return y
        

    def makeWaves(self):
        '''
        Creates wave plot by layering sine/cosine waves
        '''
        
        
        f, ax = plt.subplots()
        for i in range(0,np.random.randint(0,100)):
            x = np.arange(0, self.array_size, 1)
            y = self.sine(x)
            print(y)
            
            ax.plot(x,y)
            ax.set_xticks([])
            ax.set_yticks([])
        plt.show()
        
if __name__=="__main__":
        
#    List of all colormaps from matplot lib: https://matplotlib.org/stable/tutorials/colors/colormaps.html
    cmaps = ['Greys', 'Purples', 'Blues', 'Greens', 'Oranges', 'Reds',
            'YlOrBr', 'YlOrRd', 'OrRd', 'PuRd', 'RdPu', 'BuPu',
            'GnBu', 'PuBu', 'YlGnBu', 'PuBuGn', 'BuGn', 'YlGn',
            'viridis', 'plasma', 'inferno', 'magma', 'cividis',
            'PiYG', 'PRGn', 'BrBG', 'PuOr', 'RdGy', 'RdBu',
            'RdYlBu', 'RdYlGn', 'Spectral', 'coolwarm', 'bwr', 'seismic']
    
    rp = randomPlotter()
    rp.makeWaves()

#    looping through colormaps to compare
#    for c in cmaps:
#        print(f'Generating plots for colormap: {c}')
#        rp.hist2d(colormap=c, savefig=True)
#        rp.plotCircles(colormap="Set1", set_title=True, savefig=True)
