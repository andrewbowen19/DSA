# Trying out the pencil-sketch snippet we found online
# Thank you, LinkedIn: https://www.linkedin.com/search/results/content/?keywords=convert%20picture%20to%20sketch%20using%20python&sid=FAM&update=urn%3Ali%3Afs_updateV2%3A(urn%3Ali%3Aactivity%3A6936627290571194368%2CBLENDED_SEARCH_FEED%2CEMPTY%2CDEFAULT%2Cfalse)

import cv2
import numpy as np
import matplotlib.pyplot as plt
import os


def pencil_sketch(image_path, ksize:int = 21):
    '''Create pencil sketch drawing version of an image'''
    image = cv2.imread(image_path)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    inverted = 255 - gray_image

    blur = cv2.GaussianBlur(inverted, ksize=(ksize, ksize), sigmaX=0)  # ksize=(21, 21)
    inverted_blur = 255 - blur
    sketch = cv2.divide(gray_image, inverted_blur, scale=256.0)
    print(sketch, type(sketch))

    # Writing to output dir
    file_name = os.path.basename(image_path).split(".")[0] + "_pencil.jpg"
    file_name = file_name.replace(".jpeg", ".jpg")
    cv2.imwrite(os.path.join("img", "sample", "output", file_name), sketch)

    return gray_image, sketch


if __name__=="__main__":

    kernels = {
               "jeff-laurel-sunset.jpg":81,
            #    "milllie-hardwood.jpg":51,
            #    "millie-boat.jpg":15,
            #    "millie-cute-as-a-button.jpg":81,
            #    "zach-balloons.jpg":25,
            #    "kristine-amelia-park.jpg": 27,
               "drew-beautiful.jpg": 7
               }

    for f in os.listdir("img/sample"):
        if ".jpg" in f:
            print(f)
            im_path = os.path.join("img", "sample", f)
            img, sketch = pencil_sketch(im_path, ksize=kernels.get(f))
            
            # cv2.startWindowThread()
            
            cv2.imshow(f, sketch)
            im_concat = np.concatenate((img, sketch), axis=1)
            compare = cv2.imshow("Side-by-side", im_concat)
            comparison_file_name = "pencil_compare" + f
            cv2.imwrite(comparison_file_name, im_concat)

            cv2.waitKey(0)

    # plt.show()



