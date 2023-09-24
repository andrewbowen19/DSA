# triangle-pixelation script
# https://scikit-image.org/docs/dev/auto_examples/segmentation/plot_rag_boundary.html#sphx-glr-auto-examples-segmentation-plot-rag-boundary-py

# skimage pixel_graph also looks interesting
# https://scikit-image.org/docs/dev/auto_examples/applications/plot_pixel_graphs.html#sphx-glr-auto-examples-applications-plot-pixel-graphs-py

import numpy as np
import os


from skimage.future.graph import rag
from skimage.future import graph
from skimage import data, segmentation, color, filters, io
from matplotlib import pyplot as plt
from PIL import Image


def get_image_data(image_path: str) -> np.ndarray:
    """Gets an image's data and returns it as a numpy array"""
    data = Image.open(image_path)
    data = data.convert("RGB")
    data = np.asarray(data)
    return data

def create_rag(img) -> None:
    """Create Sklearn region-adjacency graph with triangular grid"""
    f, ax = plt.subplots()
    gimg = color.rgb2gray(img)

    labels = segmentation.slic(img, compactness=50, n_segments=200, start_label=1)
    edges = filters.sobel(gimg)
    edges_rgb = color.gray2rgb(edges)

    g = graph.rag_boundary(labels, edges)
    print("G-Unit:", g)
    lc = graph.show_rag(labels, g, edges_rgb, img_cmap='PuBuGn', edge_cmap=None, # 'PuBuGn',
                        edge_width=0.0)

    io.show()



if __name__ == "__main__":

    img_path = os.path.join("..", "img", "proposal.png")
    img_data = get_image_data(img_path)
    
    # print(f"Image array shape: {img_data.shape}")
    create_rag(img_data)
