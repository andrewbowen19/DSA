# dsa/random/src/for_mom.py

import matplotlib.pyplot as plt
import numpy as np
np.seterr(all="ignore") # Ignore Numpy warnings
import os
import uuid
from matplotlib.tri import Triangulation

"""
Script containing the code for my christmas present to my mom.

Inscription:
- - - - - -
Mom,

I made this for you!
I know it may seem like gobbledy-gook,
    but I made this art with code so you could always re-produce it (sort of).
This code produces images based on sets of randomly-generated numbers.

In addition to (I think) looking cool,
    it also reminds me of the part randomness plays in all out lives.
I'm really lucky to have you as a mother, couldn't have asked for a better one.
I hope you like the prints.

Merry Christmas! Love you lots!

Andrew
"""


class forMom:

    def __init__(self, array_size, cmap='Set1', axes_lines: bool = False):
        '''
        Class to create a 4-panel plot for mom for Christmas
        The 4 panels should contain one
            of each sub-plot produced by other class methods
        '''
        self.array_size = array_size
        self.axes_lines = axes_lines
        self.cmap = cmap

    def hist2d(self, savefig=False):
        '''
        Creates 2D histogram

        parameters:
            colormap : str; matplotlib.pyplot colormap name
            savefig : boolean (default false); if True,
                        figure is saved to plots/hist2d directory
        '''
        x = np.arange(0, self.array_size, 1)
        y = np.random.random(x.size)

        f, ax = plt.subplots(figsize=(10, 10))
        ax.hist2d(x, y, cmap=self.cmap, bins=[25, 25])
        ax.set_xticks([])
        ax.set_yticks([])

        ax.axis('off')

        # Saving the figure
        if savefig:
            if not os.path.isdir(os.path.join(".", "plots",
                                              "hist2d",
                                              f"hists_{self.array_size}")):
                os.mkdir(os.path.join("..", "plots",
                                      "hist2d", f"hists_{self.array_size}"))

            file_name = f"mom_hist2d_{self.cmap}_{self.array_size}.pdf"
            file_path = os.path.join("..",
                                     "plots", "mom_proofs",
                                     file_name)
            f.savefig(file_path)

    def triplot(self, savefig: bool = False):
        '''
        Creates triplot (mesh) from randomly-generated data

        parameters:
            savefig : boolean (default false); if True,
                        figure is saved to plots/hist2d directory
        '''
        gridsize = 3
        f, axs = plt.subplots(gridsize, gridsize, figsize=(8, 8))

        # generating triangle points and vertices coords
        x = np.random.uniform(0, 5, 100)
        y = np.random.uniform(0, 5, 100)
        triples = np.random.randint(0, 100, size=(x.size, 3))

        # Generating color and triangulation obj
        C = np.random.randint(10, size=x.size)
        triangles = Triangulation(x, y, triples)

        # Creating grid of pattern
        alpha = 0.1
        for i in range(0, gridsize):
            for j in range(0, gridsize):
                alpha = np.random.random()
                axs[i, j].tripcolor(triangles,
                                    facecolors=C,
                                    cmap=self.cmap,
                                    alpha=alpha)
                axs[i, j].set_axis_off()

        # Saving figure
        if savefig:
            index = np.random.randint(0, 10000)
            triplot_name = f"triplot_{self.cmap}_{index}_mom_proof.pdf"
            f.savefig(os.path.join("..", "plots",
                                   "mom_proofs",
                                   triplot_name))

    def get_scatter_data(self):
        '''
        Generates random data for a colored scatter plot
        '''
        # Generating x, y, size & color arrays
        x = np.random.random(self.array_size)
        y = np.random.random(self.array_size)
        s = np.random.randint(0, 50, self.array_size)
        c = np.random.random(self.array_size)

        return x, y, s, c

    def get_gauss_data(self):
        '''Generates random sigma and mu values for gaussian overlay plot'''
        mu = np.random.randint(0, 1000, self.array_size)
        sigma = np.random.randint(0, 1000, self.array_size)
        x = np.linspace(0, 1000)

        return x, mu, sigma

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
            savefig : boolean, default True;
                if True, saves figure created as PDF
        '''

        f, ax = plt.subplots()

        for m, s in zip(mu, sigma):
            r = np.random.random()
            g = np.random.random()
            b = np.random.random()
            c = (r, g, b)
            ax.plot(x, np.random.random() * self.gauss(x, m, s), color=c)
            ax.plot(x, np.random.random() * -self.gauss(x, m, s), color=c)

        ax.set_xticks([])
        ax.set_yticks([])
        title = uuid.uuid4().hex
        ax.set_title(title)

        if self.axes_lines:
            ax.axis('off')

        if savefig:
            plot_path = os.path.join('.',
                                     'plots', 'waves',
                                     f'waves_gauus_{title}.pdf')
            f.savefig(plot_path)
        self.f_gauss = f
        self.ax_gauss = ax

    def hist_data(self):
        '''
        Creates 2D histogram data arrays
        '''
        x = np.arange(0, self.array_size, 1)
        y = np.random.random(x.size)

        return x, y

    def contour_data(self):
        '''
        Randomly generates data arrays for contour plot (X, Y, Z)
        '''
        x = np.linspace(-10, 10, self.array_size)
        y = np.linspace(-10, 10, self.array_size)

        # Generating random coeffs
        a = np.random.random()
        b = np.random.random()

        X, Y = np.meshgrid(x, y)
        Z = np.sin((a*X)) + np.cos((b*Y))

        return X, Y, Z

    def panel_plot(self):
        '''
        Creates 2x2 panel plot from the "data" generated by the above methods
        '''
        f, axs = plt.subplots(2, 2, figsize=(8, 8))

        # Creating 2-d histogram
        x, y = self.hist_data()
        axs[1, 1].hist2d(x, y, cmap=self.cmap, bins=[25, 25])

        # Creating scatter plot -- upper left
        x, y, s, c = self.get_scatter_data()
        axs[0, 0].scatter(x, y, s, c=c, cmap=self.cmap)

        # Creating Gaussian Waves
        x, mu, sigma = self.get_gauss_data()
        for m, s in zip(mu, sigma):
            axs[0, 1].plot(x, self.gauss(x, m, s), alpha=np.random.random())

        # Creating contour plot -- lower right
        X, Y, Z = self.contour_data()
        axs[1, 0].contourf(X, Y, Z, levels=6, cmap=self.cmap)

        # Getting rid of axes ticks
        for axis in axs:
            for a in axis:
                a.set_xticks([])
                a.set_yticks([])
                a.axis('off')

        self.f_panel = f
        self.ax_panel = axs

        output_path = os.path.join("..", "plots", f"for_mom.pdf")
        f.savefig(output_path)


if __name__ == "__main__":
    # generating random number for index of output plot
    r = np.random.randint(0, 10000)
    print(f'Size: {r}')
    fm = forMom(5000, axes_lines=True, cmap='Set1')

    # Create 2d hist with the colormap you like
    fm.cmap = 'plasma'
    fm.hist2d()

    # generating 2d hist with reverse colormap too
    fm.cmap = fm.cmap + "_r"
    fm.hist2d()

    # Create triplot
    fm.triplot()

    # Create panel_plot
    fm.cmap = 'Set1'
    fm.panel_plot()

    plt.show()

    # Saving to plots dir -- os.path this
    file_name = os.path.join('..', 'plots',
                             'mom_proofs', f'mom_panel_{r}_{fm.cmap}.pdf')
    print(f'Saving to filepath: {file_name}')
    fm.f_panel.savefig(file_name)
