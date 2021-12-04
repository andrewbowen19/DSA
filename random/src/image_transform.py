#dsa/random/image_transform.py

import numpy as np
import matplotlib.pyplot as plt
import imageio as im
import os



class Fourier(object):

    def __init__(self):
        print('Making Fourier proud...')

    def read_image(self, img_path):
        '''Reads in image file from specified path'''

        self.img = im.imread(img_path)
#        plt.imshow(self.img)
        

    def create_fourier_transform(self):
        '''Calculates fast fourier transform and plots it'''
        
        fourier = np.fft.fft2(self.img)
        fourier_im = np.fft.ifft2(self.img)
        print(fourier)
        
#        plt.imshow(np.real(fourier))
#        plt.imshow(np.real(fourier_im))

#        Reversing back to 'original' image
        reverse = np.fft.fft2(fourier)
        print('Reverse', reverse)
        plt.imshow(np.real(reverse), cmap=plt.cm.viridis)#, vmin=100, vmax=255)
        
        plt.xticks([])
        plt.yticks([])

    def make_color_grid(self):
        '''Creates colormap grid of input img'''
        
        f,axs = plt.subplots(3,3)
        print(self.img.shape)
#        O(n) hates him.
        for i in range(0,3):
            for j in range(0,3):
                axs[i,j].imshow(self.img, alpha=0.5)
        
        
#       No ticks
        for axis in axs:
            for a in axis:
                a.set_xticks([])
                a.set_yticks([])
#                a.axis('off')

        

if __name__=="__main__":
    mill_path = os.path.join('.', 'img', 'millie.png')
    f = Fourier()
    f.read_image(mill_path)
#    f.create_fourier_transform()
    f.make_color_grid()
    
    plt.show()
