import numpy as np
from PIL import Image

data = np.zeros((1000, 1000, 3), dtype=np.uint8)
# Creating a canvas
data[:] = [123, 11, 25]

# Making a Patch
data[99:901, 99:901] = [255, 0, 0]

img = Image.fromarray(data, mode='RGB')
img.save('canvas.png', bitmap_format='png')
