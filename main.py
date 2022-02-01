import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageOps

#image must be in the same path as this program 
img_name = "frog.jpeg"

img = np.array(Image.open(img_name))

plt.figure(figsize = (8, 8))
plt.imshow(img)
plt.show()

new_img = img.copy()
new_img = 255 - new_img
plt.title("negative of rgb")
plt.imshow(new_img)
plt.show()


print("worked")
