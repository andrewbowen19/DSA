#dsa/random/mondrianMaker.py

import os
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap
import uuid



class mondrian():

    def __init__(self):
        '''Generates a randomly produced Mondrian-style image'''
        print('Whaddup Piet!?')
        self.cmap = self.create_colormap()

    def create_colormap(self):
        '''
        Creates matplotlib linear segmented colormap
        
        https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LinearSegmentedColormap.html
        
        '''
#        Mondrian-style colors
        colors = ["#ffffff", "#225095", "#dd0100", "#fac901"]
        cmap = LinearSegmentedColormap.from_list("Mondrian", colors, N=len(colors))
        return cmap

    def mondrian_maker(self, savefig=False):
        """
        Let's make some Mondrian's
        """
#        generating random bin edges for
        bin_sizes = np.random.randint(5,12)
        x_bins = sorted(np.random.rand(bin_sizes))
        y_bins = sorted(np.random.rand(bin_sizes))

#        print(x_bins, y_bins)
        
        x = np.random.random(100)
        y = np.random.random(100)
        
#        Create a colormap and plotting
        cmap = self.cmap  #create_colormap()
        plt.hist2d(x,y, bins=[x_bins, y_bins], cmap=cmap)
        plt.hlines(y_bins, xmin=0, xmax=1, color='0', linewidths=4)
        plt.vlines(x_bins, ymin=0, ymax=1, color='0', linewidths=4)
        
        plt.xticks([])
        plt.yticks([])
        
        title = uuid.uuid4().hex
        print(title)
        plt.title(title)
        
#        plt.show()
        if savefig:
            plt.savefig(os.path.join("plots", "mondrian", f"mondrian_{title}.pdf"))
        
        plt.close()



if __name__=="__main__":
    m = mondrian()
    n_plots = np.random.randint(5,100)
    print(f'Generating {n_plots} mondrian plots')
#    Generating some # of plots
    for _ in range(0,n_plots):
        m.mondrian_maker(savefig=True)

