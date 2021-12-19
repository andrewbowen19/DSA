# image_recreate/jeffAndLaurel.py

from imageRecreate import imageRecreate
import os
from sys import argv

if __name__=="__main__":
    cmap = 'PuRd'
    raw_image_path = os.path.join('.', 'data', 'jeff-laurel-proposal.png')
    
#    Allow user to pass command-line arguments if they want to change the colormap/input image
    try:
        raw_image_path = argv[1]
        cmap = argv[2]
        
    except:
        pass

#    Recreate the image.
    ir = imageRecreate(cmap=cmap)
    ir.create_panel(raw_image_path)
    
    print('Merry Christmas! Love you both.')
