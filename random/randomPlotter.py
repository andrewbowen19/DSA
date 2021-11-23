# Plot some randomness!
#dsa/random/random.py

'''Script to generate plots of random datasets'''

import os
import numpy as np
import matplotlib.pyplot as plt
import uuid
import seaborn as sns

class randomPlotter(object):

    def __init__(self):
        '''Class to generate plots based on randomness'''
        self.array_size = np.random.randint(0, 20000)
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
            
            if not os.path.isdir(".", "plots", "hist2d", f"hists_{self.array_size}"):
                os.path.mkdir(os.path.join(".", "plots", "hist2d", f"hists_{self.array_size}"))
            
            file_path = os.path.join(".", "plots", "hist2d", f"hists_{self.array_size}", f"hist2d_random_{colormap}_{self.array_size}.pdf")
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
        a = np.random.uniform(-1,1)
        b = np.random.uniform(-1,1)
        c = np.random.uniform(-1,1)
        d = np.random.uniform(-1,1)
        print(f'Coefficients: a: {a} | b: {b} | c: {c} | d:{d}')
        y = a * np.sin(((1/b) * x) + c) + d
        return y
        

    def makeWaves(self):
        '''
        Creates wave plot by layering sine/cosine waves
        '''
        
        f,ax = plt.subplots(figsize = (8,5))

        X = np.arange(0,1000,1)
        for x in np.arange(0,50,1):#plots 50 curves
            r1 = np.random.rand()
            r2 = np.random.rand()
            r3 = np.random.rand()
            r4 = np.random.rand()
            op_function = r1 * (np.sin(r2 * X) ** r3) + r4
            ax.plot(X, op_function)
            ax.set_xticks([])
            ax.set_yticks([])
            plt.show()
    
    def chaotic_sine(x, mu, sig, wave_type='sine'):
        '''
        Returns sine or cosine dis
        '''
    
        if wave_type=="sine":
            return np.sin((X **2) * np.exp(-np.power(x - mu, 2.) / (2 * np.power(sig, 2.))))
        elif wave_type=='cosine':
            return np.cos(X * np.exp(-np.power(x - mu, 2.) / (2 * np.power(sig, 2.))))
        else:
            return np.sin(np.random.random() * x)
    
    def gauss(self, x, mu, sig):
        '''
        Returns Gaussian for an input array
        
        parameters:
            x : array-like; input points to calculate gaussian dist for
            mu : int or float; mean of distribution
            sig : int or float; std dev of distribution
        '''
        return np.exp(-np.power(x - mu, 2.) / (2 * np.power(sig, 2.)))
        
    def make_gauss_waves(self, x, mu, sigma, save_fig=True):
        '''
        Creates overlaid Gaussian wave-packet plots
        
        parameters:
            
        '''
        
        f,ax = plt.subplots()
        
        for m, s in zip(mu, sigma):
            ax.plot(x, np.random.random() * self.gauss(x, m, s))
            ax.plot(x, np.random.random() * -self.gauss(x, m, s))
        
        ax.set_xticks([])
        ax.set_yticks([])
        title = uuid.uuid4().hex
        ax.set_title(title)
        
        if save_fig:
            plot_path = os.path.join('.', 'plots', 'waves', f'waves_gauus_{title}.pdf')
            f.savefig(plot_path)
        
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
    
    ass = rp.array_size
#    rp.makeWaves()


#    looping through colormaps to compare
#    for c in cmaps:
#        print(f'Generating plots for colormap: {c}')
##        rp.hist2d(colormap=c, savefig=True)
#
#        rp.plotCircles(colormap=c, set_title=True, savefig=True)
#        plt.close()
        

#    Gauss waves
    m = np.random.randint(0,1000, 1000)
    s = np.random.randint(0,1000, 1000)
    x = np.linspace(0,1000)
    rp.make_gauss_waves(x, m, s)
