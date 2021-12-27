# dsa/random/hatched_contour.py

# https://matplotlib.org/stable/gallery/images_contours_and_fields/contourf_hatching.html#sphx-glr-gallery-images-contours-and-fields-contourf-hatching-py

import matplotlib.pyplot as plt
from matplotlib.tri import Triangulation
from matplotlib.patches import Polygon
import numpy as np
import uuid
import os

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

def hatch_plot(x_func=None, y_func=None, hatches=None, savefig:bool=False):
    # invent some numbers, turning the x and y arrays into simple
    # 2d arrays, which make combining them together easier.
    x = np.arange(0, 10, 1).reshape(1, -1)
    y = np.arange(0,  10, 1).reshape(-1, 1)

    # If functions specified by user, use those
    if x_func and y_func:
        z = np.random.uniform(-10,10,1) * x_func(x) * np.random.uniform(-10,10,1) * y_func(y)
    else:
        coeffs = np.random.uniform(0, 10, 4)
        print(f'Fucntion Coefficeints: {coeffs}')
        z = coeffs[0] * np.cos(coeffs[1] * x) + coeffs[2] * np.sin(coeffs[3]* y)

    # we no longer need x and y to be 2 dimensional, so flatten them.
    x, y = x.flatten(), y.flatten()

    f, ax = plt.subplots()
    # picking random colormap and alpha
    ic = np.random.randint(0,len(cmaps)-1)
    alpha = np.random.random()
    ax.contourf(x, y, z, hatches=hatches,
                    cmap=cmaps[ic], alpha=alpha) # extend='both',

    ax.set_axis_off()

    # plt.show()

    if savefig:
        id = uuid.uuid4().hex
        file_path = os.path.join("..", "plots",
                            "contour", "hatched",
                            f"contour_hatched_{cmaps[ic]}_{id}.pdf")
        print(f'Saving file with ID: {id}')
        f.savefig(file_path, bbox_inches='tight')
        plt.clf()

def diamond_plot(n=5):
    '''Create Diamond overlay'''
    f, ax  = plt.subplots()

    for _ in range(n):
        size = np.random.randint(3,100)
        data = np.random.rand(size,2)
        x = data[:,0]
        y = data[:,1]
        
        print(x.shape, y.shape)
        print(x.size, y.size)

        triangles = Triangulation(x, y)

        z = np.cos(x) + np.random.random() * np.sin(y)

        # Generating colors of plot
        r = np.random.random()
        g = np.random.random()
        b = np.random.random()

        c = (r, g, b)

        ax.triplot(triangles, color=c)

        ax.set_axis_off()

def yusyuki():
    '''Take 2 of trying to make a Yusyuki using matplotlib.'''
    # Setting up array of polygon corners
    # starting Trapezoid
    # corners = np.asarray([[0,0],[1,1],[2,1],[3,0]])
    
    f, ax = plt.subplots()
    hatches =["\\", "//"]
    colors = ['orange', 'blue']
    
    for i in range(10):
        corners = np.random.rand(4,2)
        print(corners)

        # Generating kwargs -- colors of plot and hatches

        c = colors[0] if  (i%2==0) else colors[1]#(r, g, b)
        h = hatches[0] if (i%2==0) else hatches[1]
        trap = Polygon(corners, fill=True, color=c, alpha=0.5,   hatch=h)
        ax.add_patch(trap)



    ax.set_axis_off()





if __name__ == "__main__":
    # x_coeff = np.random.uniform(0,100,1)
    # y_coeff = np.random.uniform(0,100,1)

    # print('Coefficients: x -> {x_coeff} | y-> {y_coeff}')
    # for _ in range(0,100):

    #     hatch_plot(hatches =['\\','/'], savefig = True)

    # diamond_plot(4)
    yusyuki()

    plt.show()
    