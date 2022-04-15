
# importing PIL Module
from PIL import Image
 
# open the original image
original_img = Image.open("martian_surface.jpg")
 
# Flip the original image vertically
vertical_img = original_img.transpose(method=Image.FLIP_TOP_BOTTOM)
vertical_img.save("vertical.jpg")
# Flip the original image horizontally
horz_img = original_img.transpose(method=Image.FLIP_LEFT_RIGHT)
horz_img.save("horizontal.jpg") 
# Display the image vertically and horizontally
vertical_img.show()
horz_img.show()
