# dsa/image_recreate/imageRecreate.py

import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import os
from sys import argv
from scipy import ndimage


import skimage.filters
import skimage.io
from skimage.filters.rank import entropy
from skimage.morphology import disk
from skimage import data, segmentation, color
from skimage.future import graph


class imageRecreate():

    def __init__(self, path=None, cmap='viridis'):
#        print('Recreating image')
        self.path = path
        self.cmap = cmap

    def read_image(self, image_path:str, as_array:bool=True, convert_to_greyscale:bool=False):
        '''Reads in image data from a source file path
        
        parameters:
            image_path : str; path to image file to be read-in
            as_array : bool, default True; if True, a numpy.ndarray is returned. If False, a Pillow.Image object is returned.
            
        returns:
            image : PIL Image object or np.array (if as_array set to True) ; raw image data from source image, can be manipulated with other class methods
        '''
        
        image = None
#        Try reading in from argument passed, if it's bad try the class attr
        try:
            if image_path:
                image = Image.open(image_path)#.convert("L")
            else:
                image = Image.open(self.path)#.convert("L")
        except:
            print('Issue reading in image file. Double-check the path')
        
        if convert_to_greyscale:
            image = image.convert("L")
        
#        Returning as array data
        if as_array:
            image = np.asarray(image)
            
        return image

    def entropy(self, image_path:str, savefig:bool=False):
        '''
        Generates entropy plot of input image.
        
        parameters:
            image_path : str; path to image we want to read in
            savefig : bool ; if True, figure is saved as pdf
            
        returns:
            entr_image : numpy.array object containing pixel data for the input image
        '''
        print('Generating entropy image...')
#        Read in image and compute image data entropy
        im_name = os.path.basename(image_path).split(".")[0]
        im = self.read_image(image_path, convert_to_greyscale=True)
        entr_img = entropy(im, disk(10))
        
#        Plotting 3 panels: raw image, image with basic colormap, entropy image with same colormap applied
        f, (ax1, ax2, ax3) = plt.subplots(nrows=1, ncols=3, figsize=(9,6),sharey=True)
        ax1.imshow(np.asarray(Image.open(image_path)))
        ax2.imshow(im, cmap=self.cmap)
        ax3.imshow(entr_img, cmap=self.cmap)
        
#        Format the figure
        for a in [ax1, ax2, ax3]:
            a.set_axis_off()
        f.tight_layout(pad=2)
        
        if savefig:
            fig_path = os.path.join(".", 'plots', 'entropy', f'entropy_{im_name}_{self.cmap}.pdf')
            f.savefig(fig_path, bbox_inches='tight', pad_inches = 1)
            
        f.clf()
        
        return entr_img
        
    def segment_image(self, image_path:str,  n, thresh, c, savefig:bool=False):
        '''
        Creates segmentation (impressionist-style) recreation of an image using scikit-image
        
        parameters:
            image_path : str; path to image we want to read in
            savefig : bool, default False ; if True, figure is saved as pdf
        '''
        im_name = os.path.basename(image_path).split(".")[0]
        im = self.read_image(image_path, True, False)
        

        print(f'Generating RAG image..')
        print(f'N Segments: {n} | Threshold: {thresh} | Compactness {c}')
        
#        Generate image segmentation plot
        labels1 = segmentation.slic(im, compactness=c, n_segments=n, start_label=1)
        out1 = color.label2rgb(labels1, im, kind='avg', bg_label=0)

#        Create Region Adjacency Graph
        g = graph.rag_mean_color(im, labels1)
        labels2 = graph.cut_threshold(labels1, g, thresh)
        out2 = color.label2rgb(labels2, im, kind='avg', bg_label=0)

#        Plot the image
        f, ax = plt.subplots(nrows=1, ncols=2, sharex=True, sharey=True,
                               figsize=(8, 5))
        ax[0].imshow(out1)
        ax[1].imshow(out2)
        
        ax[0].set_axis_off()
        ax[1].set_axis_off()
        
#        Save the figure if desired
        if savefig:
            f.savefig(os.path.join('plots','segmentation', f'segmentation_{im_name}_{n}_{thresh}_{c}.pdf'))
        
        return out2
        
    def create_panel(self, image_path:str, savefig:bool=False):
        '''
        Create 2x2 panel print contianing colormap, entropy, and RAG images
        '''
        
#        Generate images
        image = self.read_image(image_path)
        cmap_im = self.read_image(image_path, convert_to_greyscale=True)
        ent = self.entropy(image_path)
        rag = self.segment_image(image_path, 1000, 40, 25)
        
#        Plot the images
        f, axs = plt.subplots(nrows=2, ncols=2, figsize = (8,6))
        axs[0,0].imshow(image)
        axs[0,1].imshow(cmap_im, cmap=self.cmap)
        axs[1,0].imshow(ent, cmap=self.cmap)
        axs[1,1].imshow(rag)
        
        for i in range(len(axs)):
            for j in range(len(axs)):
                axs[i,j].set_axis_off()
        f.tight_layout(pad=2)
            
        if savefig:
            file_name =os.path.basename(image_path).split('.')[0]
            file_path = os.path.join(file_name + "_panel.png")
            f.savefig(os.path.join('plots', f'.png'), bbox_inches='tight')
        
        return f, axs

            
if __name__=="__main__":

#    Default input path/cmap
    input_path = os.path.join(os.path.join('img', 'jeff-laurel-proposal.png')
    cmap = 'PuRd'
    
#    Get command line args if they are passed by the user
    try:
        input_path = argv[1]
        cmap = argv[0]
        
    except:
        pass
        
#    Create the image
    ir = imageRecreate(cmap='PuRd')
    ir.create_panel(input_path)

