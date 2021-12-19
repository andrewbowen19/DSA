# image_recreate/old/old.py

# Old image visualization functions DEPRECATED
# for updated formatting/code look at imageRecreate

from imageRecreate import read_image
import skimage
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import os
from scipy import ndimage


import skimage.filters
import skimage.io
from skimage.filters.rank import entropy
from skimage.morphology import disk
from skimage import data, segmentation, color
from skimage.future import graph

def streamplot(self, source_image_path:str):
    '''
    Recreates matplotlib.pyplot.streamplot image from source
    
    parameters:
        
    '''
    
    im = read_image(source_image_path)
    print(im, im.shape, im.size)

    x = np.arange(0, im.shape[0], 1)
    y = np.arange(0, im.shape[1], 1)
#       Getting gradient 'vector fields'
    sx = ndimage.sobel(im, axis=0, mode='constant')
    sy = ndimage.sobel(im, axis=1, mode='constant')
    
    print(x.shape, y.shape, sx.shape, sy.shape)

#        Plotting streamplot
    f,ax = plt.subplots()
    ax.streamplot(x,y,sx.flatten(),sy.flatten())
    
    
    ax.set_axis_off()

def convert_image(self, image_path):
    '''Want to checkout grayscale image format'''
    
#        Reading in image and converting data to grayscale ("L")
    image = Image.open(image_path, formats=['png'])
    image = image.convert("L")
    
    im = np.asarray(image)
    print('Raw image data: ', im)
    print('Image size, shape: ', im.size, im.shape)
    x = np.zeros_like(im)
    
#        Adding white noise to image data
    im_white_noise = add_white_noise(im, 0.1)
    print("Image data (white-noise added): ", im_white_noise)
    plt.imshow(im_white_noise)
    
    lengths = [500]#, 100, 200]
    
    print('################################################')
    for l in lengths:
        print(f'Generating LIC image with length: {l}')
        lic_result = lic.lic(x, im_white_noise, length=l)
        f,ax = plt.subplots()
        ax.imshow(lic_result, cmap='gray')
        
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_title(f'Length: {l}')
        
        f.savefig(f'plots/sample_lic_{l}.pdf')
        f.clf()

#        plt.imshow(lic_result, origin='lower', cmap='gray')
    
    plt.show()
    
@staticmethod
def add_white_noise(image, prob):
    '''Add white noise to image data'''
    output = np.zeros(image.shape)
    thres = 1 - prob
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rdn = np.random.random()
            
            if rdn < prob:
                output[i][j] = 0
            if rdn > thres:
                output[i][j] = 255
                
            else:
                output[i][j] = image[i][j]
    return output

def calculate_lic(self, image_path:str, savefig:bool):
    '''
    Calculates the LIC array from the gradient vector of an image
    
    Using this python module: https://rufat.be/licpy/
    GitHub repo:
        https://github.com/drufat/licpy
    May fork and improve a bit
    '''
    input_file_name = os.path.basename(image_path).split('.')[0]
    im = read_image(image_path, True)
    
    im = add_white_noise(im, 0.2)
#        https://stackoverflow.com/questions/49732726/how-to-compute-the-gradients-of-image-using-python
    # Get x-gradient in "sx" and y-gradient in 'sy'
    sx = ndimage.sobel(im, axis=0, mode='constant')
    sy = ndimage.sobel(im, axis=1, mode='constant')
    
#        Generating Line Integral Convolution array with given streamline len
    length = 10
    tex = runlic(sx, sy, length)
    print('LIC output: \n', tex)
    
#        Logging output array to save compute
    with open(os.path.join('logs', f'tex_{input_file_name}_{length}.txt'), 'w') as f:
        for row in tex:
            np.savetxt(f, row)
    
    f,ax = plt.subplots()
    ax.imshow(tex, cmap='gray')
    ax.set_axis_off()
    ax.set_title(os.path.basename(image_path))
    
    if savefig:
        index = np.random.randint(0,10000)
        plot_path = os.path.join('.', 'plots', f'lic_output_{length}_{input_file_name}.pdf')
        f.savefig(plot_path)

def apply_gaussian_filter(self, image_path):
    '''
    Apply gaussian filter to an image (datacarpentry)
    '''
    im = read_image(image_path)
    blurred = skimage.filters.gaussian(im, sigma=(25, 25))
    
    print(blurred)
    
    skimage.io.imshow(blurred)
    
def laplacian_filter(self, image_path):
    '''Apply Laplacian filter to image data'''
    f, (ax1, ax2) = plt.subplots(nrows=1, ncols=2)

    im = read_image(image_path)
    laplace = skimage.filters.laplace(im)
    
    ax1.imshow(im)
    ax2.imshow(laplace)
    ax1.set_axis_off()
    ax2.set_axis_off()
