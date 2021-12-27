# image_recreate/jeffAndLaurel.py

"""
This script produces my christmas gift for my brother and his new* fiancé.

Example output here:
https://github.com/andrewbowen19/dsa/tree/main/image_recreate#output-example

In order to run this script you'll need to have python installed on your computer.
Install Python here: https://www.python.org/downloads/

To run this script, use the directions found in the README in this folder.

Message to the recipients:
- - - - - - - - - - - - -

Jeff & Laurel,

Merry Christmas! I really hope you guys like the images produced by this code.
The day Jeff proposed, we all felt so much joy being able to 'formally' welcome Laurel as a part of the family.
I wish you guys all the happiness in the world as you start to go down this journey.

I struggled trying to find a good way to edit the picture of y'all immediately after the proposal.
Jeff gave me the intel that Laurel's favorite color is pink, so that's where the colormap comes from.
The pictures on the bottom are re-generated from a python machine-learning library.
    The left one is the entropy of the source image. This shows a lot of the edges and sharp changes in the image data.
    The right image's formal name is a Region-Adjacency Graph. This is a fancy name for saying that it merges regions of the painting with like colors
        It makes the image appear more like a painting with really blotchy brushstrokes.

Jeff -- I'm so proud of you man. You were always someone I really looked up to, and still do.
Laurel -- You've become like a sister to me and I'm so glad that you're officially becoming part of the family.
    (even though let's be honest, you basically already were).

No need to hang the print-out if it doesn't suit your style, I just wanted to have something to give y'all in addition to the code.
If you want me to change anything with the images/get them re-printed I'm happy to do it!

Love you both. Merry Christmas!!!
"""

from imageRecreate import imageRecreate
import os
from sys import argv
import matplotlib.pyplot as plt


if __name__ == "__main__":
    # Allow user to pass command-line arguments if they want to change the colormap/input image
    try:
        raw_image_path = argv[1]
        cmap = argv[-1]
    except:
        cmap = 'PuRd'
        raw_image_path = os.path.join('.', 'img',
                                      'jeff-laurel-proposal-big.png')

    # Recreate the image.
    ir = imageRecreate(cmap=cmap)
    ir.create_panel(raw_image_path, True)

    plt.show()

    print('Merry Christmas! Love you both.')
