# Plot some randomness!
#dsa/random/random.py

'''Script to generate plots of random datasets'''

import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import PatchCollection
from matplotlib.patches import Ellipse
from matplotlib.tri import Triangulation
import matplotlib
import uuid
import seaborn as sns

class randomPlotter(object):

    def __init__(self):
        '''Class to generate plots based on randomness'''
        self.array_size = np.random.randint(0, 10000)
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

        f, ax = plt.subplots(figsize=(10,10))
        ax.hist2d(x, y, cmap = colormap, bins=[25,25])
        ax.set_xticks([])
        ax.set_yticks([])
        
        ax.axis('off')
        
#        Saving the figure
        if savefig:
            
            if not os.path.isdir(os.path.join(".", "plots", "hist2d", f"hists_{self.array_size}")):
                os.mkdir(os.path.join("..", "plots", "hist2d", f"hists_{self.array_size}"))
            
            file_path = os.path.join("..", "plots", "hist2d", f"hists_{self.array_size}", f"hist2d_random_{colormap}_{self.array_size}.pdf")
            f.savefig(file_path)
#        plt.close()
        
    def plotCircles(self, colormap="viridis", set_title=False, savefig=False):
        '''
        Creates scatter plot of randomly sized circles
        '''
#        Generating x, y, size & color arrays
        x = np.random.random(self.array_size)
        y = np.random.random(self.array_size)
        s = np.random.randint(0,50, self.array_size)
        c = np.random.random(self.array_size)
        
        f, ax = plt.subplots()
        ax.scatter(x,y,s, c=c, cmap=colormap)
        ax.set_xticks([])
        ax.set_yticks([])
        
        ax.axis('off')
        
        # Setting figure title/saving figure if desired
        title_hash = ''
        if set_title:
            title_hash = uuid.uuid4().hex
            ax.set_title(title_hash)
            
        if savefig:
            file_path = os.path.join("..", "plots", "scatter", f"scatter_random_{colormap}_{self.array_size}.pdf")
            f.savefig(file_path)
            
        
    def makeWaves(self):
        '''
        Creates wave plot by layering sine/cosine waves
        '''
        
        f,ax = plt.subplots(figsize = (8,5))

        X = np.arange(0,1000,1)
        for x in np.arange(0,50,1): #plots 50 curves
            r1 = np.random.rand()
            r2 = np.random.rand()
            r3 = np.random.rand()
            r4 = np.random.rand()
            op_function = r1 * (np.sin(r2 * X) ** r3) + r4
            ax.plot(X, op_function)
            ax.set_xticks([])
            ax.set_yticks([])
#            plt.show()
    
    def chaotic_sine(x, mu, sig, wave_type='sine'):
        '''
        Returns sine or cosine dis
        '''
    
        if wave_type=='sine':
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
        
    def make_gauss_waves(self, x, mu, sigma, savefig=True):
        '''
        Creates overlaid Gaussian wave-packet plots
        
        parameters:
            x : array-like; input array to create Gaussian dist
            mu : int or float; mean of dist (randomly-generated)
            sigma : int or float; std dev of gaussian dist
            savefig : boolean, default True; if True, saves figure created as PDF
        '''
        
        f,ax = plt.subplots()
        color_scheme = ['#598234', '#AEBD38', '#68829E', '#505160']
        for m, s in zip(mu, sigma):
            r = np.random.uniform(0,0.2)
            g = 0.7#np.random.random()
            b = np.random.uniform(0,0.5)
            c_index = np.random.randint(0,3)
            
            ax.plot(x, np.random.random() * self.gauss(x, m, s), color=(r,g,b))#color_scheme[c_index])#(r,g,b))
            ax.plot(x, np.random.random() * -self.gauss(x, m, s), color=(r,g,b))#color_scheme[c_index])#(r,g,b))
        
        ax.set_xticks([])
        ax.set_yticks([])
        title = uuid.uuid4().hex
        ax.set_title(title)
        
        if savefig:
            plot_path = os.path.join('.', 'plots', 'waves', f'waves_gauus_{title}.pdf')
            f.savefig(plot_path)
        
#        plt.show()
    
    def quiver_plot(self, savefig=False):
        '''
        Creates vector-field style "quiver" plot
        
        Sample here: https://matplotlib.org/stable/plot_types/arrays/quiver.html#sphx-glr-plot-types-arrays-quiver-py
        '''
        x = np.arange(-100,100, 1)
        y = np.arange(-100,100, 1)
        
        
        X, Y = np.meshgrid(x,y)
        
#        Setting up arrow direction/angles
        U = np.random.random(size=X.shape)
        V = np.random.random(size=Y.shape)
        angles = np.random.random(size=X.shape) * 360
        c = np.random.random(X.size)
        
        # print('Arrow coords: ', X, Y)
        # print('Arrow directions: ', U, V)
        print('Arrow angles', angles)
        
        
        f, ax = plt.subplots()
        ax.quiver(X, Y, U, V, c,
                    units='inches',
                    angles='xy', width=.15)
                    
        # Setting title and removing axes ticks
        title = uuid.uuid4().hex
        ax.set_title(title)
        ax.set_xticks([])
        ax.set_yticks([])
        # plt.show()
    
        if savefig:
            f.savefig(os.path.join("..", "plots", "quiver", "quiver", f"quiver_{title}.pdf"))
            
    def contour(self, x_func, y_func, cmap='viridis', threeD:bool=False, savefig:bool=False):
        '''creates artsy contour plot
        
        parameters:
            x_func, y_func: functions; applied to x and y data arrays, respectively
            cmap : str; matplotlib colormap
            threeD : bool, default False; if True, plot the contour in a third dimension (trippy, man)
            savefig : bool, default False; if True, save figure generated to a pdf
        '''
        
        x = np.arange(-10,10, 1)
        y = np.arange(-10,10, 1)
        
#        random constants to scale our x and y arrays
        a = np.random.random()
        b = np.random.random()
        c = np.random.randint(1,10)
        
        X, Y = np.meshgrid(x, y)
        Z = x_func(a*X) + y_func(b*Y)
        levels = np.random.randint(5,10)
        title = uuid.uuid4().hex
        
        if threeD:
            f = plt.figure()
            ax = plt.axes(projection='3d')
            ax.contour3D(X, Y, Z,levels=100, cmap=cmap)
#            ax.set_xlim(0,100)
#            ax.set_ylim(0,100)
#            ax.set_zlim(0,100)
#            f.add_axes(ax)
            
        else:
            f, ax = plt.subplots()
            ax.contourf(X, Y, Z, levels=levels, cmap=cmap)
            
            
        ax.set_title(title)
        ax.set_xticks([])
        ax.set_yticks([])
        ax.axis('off')
        plt.show()
    
        if savefig:
            f.savefig(os.path.join("..", "plots",
                                   "contour", f"contour_{cmap}_{title}.pdf"))

        # plt.close()
            
    @staticmethod
    def lin_model(m, x, b):
        return m*x + b
    
    def gridlines(self):
        '''
        Creates weaving pattern of grid lines
        '''
        print('Greating gridlines plot...')
        m = np.random.random()
        x = np.arange(-100,100,1)
        b = -100
        
        f,ax = plt.subplots()
        print(f'Default slope: {m}')
        for i in range(0,50):
            y = self.lin_model(m, x, b)
            z = self.lin_model(-m, x, b)
            b += 50

            ax.plot(x,y, color=str(np.random.random()))
            ax.plot(x,z, color=str(np.random.random()))
            
        
        ax.set_xticks([])
        ax.set_yticks([])
    
    def ellipses(self, cmap:str = 'BrBG', set_title:bool = False, savefig:bool=False):
        '''Plots randomly generated ellipses and fill in intersections'''
        
        f,ax = plt.subplots()
        ax.set_xlim(-10, 10)
        ax.set_ylim(-10, 10)
        
        for _ in range(0, 30):
            
#            Generate annulus obj
            x = np.random.uniform(-10, 10)
            y = np.random.uniform(-10, 10)
            width = np.random.uniform(0, 15)
            height = np.random.uniform(0, 15)

            angle = np.random.uniform(0, 360)
            
            # r = np.random.random()
            # g = np.random.random()
            # b = np.random.random()
            cmap = matplotlib.cm.get_cmap(cmap)
            c = np.random.random()

            ellipse = Ellipse((x,y), width, height, angle, color=cmap(c), alpha=np.random.uniform(0,1))
            ax.add_patch(ellipse)
            
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_axis_off()

        title = uuid.uuid4().hex
        if set_title:
            
            ax.set_title(title)

        # Saving figure
        if savefig:
            fig_path = os.path.join("..", 'plots', 'ellipses', f'ellipses_{title}.pdf')
            f.savefig(fig_path)
            
    def triplot(self, savefig:bool=False):
        '''
        Creates triplot (mesh) from randomly-generated data
        '''
    
        gridsize = 3
#        np.random.seed(10131963)
        f, axs = plt.subplots(gridsize,gridsize, figsize=(8,8))
        
        #        generating triangle points and vertices coords
        x = np.random.uniform(0,5,100)
        y = np.random.uniform(0,5,100)
        triples = np.random.randint(0,100, size=(x.size, 3))
        
#        Generating color and triangulation obj
        C = np.random.randint(10,size=x.size)
        triangles = Triangulation(x, y, triples)
   
#        Creating grid of pattern
        alpha = 0.1
        for i in range(0,gridsize):
            for j in range(0,gridsize):
                alpha = np.random.random()
                axs[i,j].tripcolor(triangles, facecolors=C,  cmap=self.cmap, alpha=alpha)
                axs[i,j].set_axis_off()
        
        if savefig:
            index = np.random.randint(0,10000)
            print(f'Tripcolor index: {index}')
            f.savefig(os.path.join("..", "plots", "triplots", f"triplot_{self.cmap}_{index}_mom_proof.pdf"))

if __name__=="__main__":
        
#    List of all colormaps from matplot lib: https://matplotlib.org/stable/tutorials/colors/colormaps.html
    cmaps = ['Greys', 'Purples', 'Blues', 'Greens', 'Oranges', 'Reds',
            'YlOrBr', 'YlOrRd', 'OrRd', 'PuRd', 'RdPu', 'BuPu',
            'GnBu', 'PuBu', 'YlGnBu', 'PuBuGn', 'BuGn', 'YlGn',
            'viridis', 'plasma', 'inferno', 'magma', 'cividis',
            'PiYG', 'PRGn', 'BrBG', 'PuOr', 'RdGy', 'RdBu',
            'RdYlBu', 'RdYlGn', 'Spectral', 'coolwarm', 'bwr', 'seismic',
            'twilight', 'twilight_shifted', 'hsv',
            'Pastel1', 'Pastel2', 'Paired', 'Accent', 'Dark2',
                      'Set1', 'Set2', 'Set3', 'tab10', 'tab20', 'tab20b',
                      'tab20c']
    
    rp = randomPlotter()
    c = "BrBG"
    rp.cmap = c
#    rp.hist2d(colormap=c, savefig=True)
#    rp.hist2d(colormap=c+"_r", savefig=True)
#    for _ in range(0,5):
#
#        rp.contour(np.sin, np.cos, 'Set1',threeD=True, savefig=True)

#    looping through colormaps to compare
#    for c in cmaps:
#        print(f'Generating plots for colormap: {c}')
#        rp.hist2d(colormap=c, savefig=True)
#
#        rp.plotCircles(colormap=c, set_title=True, savefig=True)
#        rp.contour(np.sin, np.cos, c, savefig=True)
#        plt.close()
        

#    Gauss waves
#    print('Creating Gauss waves')
#    m = np.random.randint(-100,100, 250)
#    s = np.random.randint(-100,100, 250)
#    x = np.linspace(-250,250)
#    rp.make_gauss_waves(x, m, s, savefig=True)
#
#    Gridlines
#    for _ in range(0,5):
#        rp.gridlines()

    ### Making Quiver Plot ###
#    for _ in range(0,5):
#        rp.quiver_plot()

    # Ellipses
    for _ in range(0,10):
       rp.ellipses(savefig=True)

    # Making ~spiky~ tripcolor plot
    # mom_cmaps = [ "BrBG", 'vlag']
    # for c in mom_cmaps:
    #     rp.cmap = c
    #     rp.triplot(savefig=True)
        
    #     rp.cmap = c + "_r"
    #     rp.triplot(savefig=True)
    
    plt.show()


