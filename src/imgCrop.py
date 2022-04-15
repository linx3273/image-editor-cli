from PIL import Image
import numpy as np
  
# Load image
image = Image.open('martian_surface.jpg')
  
# Convert image to array
image_arr = np.array(image)
  
# Crop image
image_arr = image_arr[100:1000, 10:450]
  
# Convert array to image
image = Image.fromarray(image_arr)
  
# Display image
image.show()