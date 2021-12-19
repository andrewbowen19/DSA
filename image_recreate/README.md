## Image Recreation

This repository serves as my attempt to explore different ways of manipulating and re-creating image data. I started this project in order to re-create an image of my brother's proposal for a Christmas gift (see below). 

### Installation
In order to install this repository, you can use `git` and `pip`. Run the following from the command line:

    git clone https://github.com/andrewbowen19/dsa.git
    
Then, change directories into this sub-repository.

    cd dsa/image_recreate
    
You can install the requirements for this project via `pip` once in the project sub-repository:

    pip install -r requirements.txt
    
### Usage
Once you've downloaded and installed the project, you can run either the main module `imageRecreate.py` or the script I wrote to create your christmas gift (`jeffAndLaurel.py`):
```
# For the main python module
python imageRecreate.py
    
# This script is customized to create a Christmas Gift for Jeff & Laurel
python jeffAndLaurel.py <Input File> <Color Map> 
```
There are a few command-line arguments that can be passed to either script. These can be used to specifiy the *input/source* image, as well as the colormap desired for the entropy image. Note that the colormap command-line argument should be a [matplotlib-style colormap](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwi84_3x-vD0AhUqUt8KHVKpCBkQFnoECAUQAQ&url=https%3A%2F%2Fmatplotlib.org%2Fstable%2Ftutorials%2Fcolors%2Fcolormaps.html&usg=AOvVaw1hdMfFfMuM8-VtgKNRXXak).

### Output Example

Source Image | Panel Output
:------------:|:------------------:
![](/img/jeff-laurel-proposal.png?raw=true) |  ![](/img/for_jeff_and_laurel.png?raw=true)

The above sub-plots are as follows: *Source/input* image (upper-left), The source image with the user-defined colormap applied (upper-right), A plot of the entropy of the image (bottom-left; calculated via [`scikit-image`](https://scikit-image.org/docs/dev/auto_examples/filters/plot_entropy.html)), The [Region-Adjacency Graph](https://scikit-image.org/docs/dev/auto_examples/segmentation/plot_rag.html) of the image.




Merry Christmas guys, hope you like it and welcome to the family, Laurel! Love you guys! 🎄❤️
