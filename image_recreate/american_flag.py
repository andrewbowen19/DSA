# american_flag.py

import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import os
import uuid
from PIL import Image
from PIL.ImageOps import mirror



class colorMap:

    def __init__(self, image_path, cmap='viridis'):
        '''Class to apply different matplotlib-style colormaps to an input image'''
        self.image_path = image_path
        self.img_file_name = os.path.basename(self.image_path).split('.')[0]
        self.cmap = cmap
        self.colormaps = [
            'viridis', 'plasma', 'inferno', 'magma', 'cividis',
            'Greys', 'Purples', 'Blues', 'Greens', 'Oranges', 'Reds',
            'YlOrBr', 'YlOrRd', 'OrRd', 'PuRd', 'RdPu', 'BuPu',
            'GnBu', 'PuBu', 'YlGnBu', 'PuBuGn', 'BuGn', 'YlGn',
            'binary', 'gist_yarg', 'gist_gray', 'gray', 'bone', 'pink',
            'spring', 'summer', 'autumn', 'winter', 'cool', 'Wistia',
            'hot', 'afmhot', 'gist_heat', 'copper',
            'PiYG', 'PRGn', 'BrBG', 'PuOr', 'RdGy', 'RdBu',
            'RdYlBu', 'RdYlGn', 'Spectral', 'coolwarm', 'bwr', 'seismic',
            'twilight', 'twilight_shifted', 'hsv',
            'Pastel1', 'Pastel2', 'Paired', 'Accent',
            'Dark2', 'Set1', 'Set2', 'Set3',
            'tab10', 'tab20', 'tab20b', 'tab20c',
            'flag', 'prism', 'ocean', 'gist_earth', 'terrain', 'gist_stern',
            'gnuplot', 'gnuplot2', 'CMRmap', 'cubehelix', 'brg',
            'gist_rainbow', 'rainbow', 'jet', 'turbo', 'nipy_spectral',
            'gist_ncar']

    def read_image(self, image_path=None, mirror_image=False):
        '''
        Reads in image data from specified path. Returned as numpy array
        
        parameters:
            image_path : str; path to image desired. If None, class attribute of image_path is used
            mirror : bool, default False; if True mirror image
        '''
        # If user specifies an image path, use it. Else use class attr
        if image_path:
            self.image_path = image_path

        # Converting image data to grayscale and numpy array
        if mirror_image:
            img = np.asarray(mirror(Image.open(self.image_path).convert('L')))
        else:
            img = np.asarray(Image.open(self.image_path).convert('L'))

        return img

    def apply_colormap(self, savefig: bool = False):
        '''Applies self.cmap to an image
        
        parameters:
            savefig : bool, default False; if True, save figure to pdf
        '''
        img = self.read_image(self.image_path, mirror_image=True)
        f, ax = plt.subplots()

        ax.imshow(img, cmap=self.cmap)
        ax.set_axis_off()

        if savefig:
            fig_path = os.path.join('plots', 'cmap', f'{self.img_file_name}_{self.cmap}.pdf')
            f.savefig(fig_path, bbox_inches='tight')

    def custom_colormap(self):
        '''Creates Matplotlib custom colormap'''

    def panel_colormaps(self, nrows=3, ncols=3, colormap='random'):
        '''
        Creates nrows x ncols panel of image with different colormaps applied
        
        parameters:
            nrows, ncols : int; # of rows/columns to make panel (default 3)
            cmap : str, default random; 
                    There are 3 options to pass for cmap
                    random - random;y generated data used for colormap
        '''
        img = self.read_image(self.image_path)#, mirror_image=True)
        f, axs = plt.subplots(nrows=nrows, ncols=ncols)

        for i in range(nrows):
            for j in range(ncols):
                # Randomly generate colormap to use
                if colormap == 'random':
                    cmap = mpl.colors.ListedColormap(np.random.rand(256,3))

                # If matplotlib style colormaps desired
                elif colormap  == 'matplotlib':
                    cmap = self.colormaps[np.random.randint(0, len(self.colormaps)-1)]

                # if user specifies one colormap, use just that one
                elif colormap in self.colormaps:
                    cmap = colormap
            
                else:
                    cmap = self.cmap

                # Plot image and remove axes lines
                axs[i, j].imshow(img, cmap=cmap)
                axs[i, j].set_axis_off()

        # Setting title for figure
        title = uuid.uuid4().hex
        f.suptitle(title)



if __name__ == "__main__":
    flag_path = os.path.join('.', 'img', 'american_flag.png')
    c = colorMap(flag_path, cmap='PuBuGn')
    c.apply_colormap()
    
    # Creating panel colormaps
    c.panel_colormaps(5,5, 'matplotlib')
    plt.show()