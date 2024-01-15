# Robot Puppy
# Emma Xu
# 12 January 2024

from PIL import Image

import colour_helper

RED_PIXEL = (150, 0 ,0)

red_ball_image = Image.open("./Images/Red Ball.jpeg")

red_pixels_x = []
red_pixels_y = []

# Visit every pixel in the image and determine those which are red
for y in range(red_ball_image.height):
    for x in range(red_ball_image.width):
        current_pixel = red_ball_image.getpixel((x,y))
        # If that pixel is red, store the location
        if colour_helper.pixel_to_string(current_pixel) == "ball red":
            red_pixels_x.append(x)
            red_pixels_y.append(y)

avg_x = sum(red_pixels_x) / len(red_pixels_x)
avg_y = sum(red_pixels_y) / len(red_pixels_y)

print(avg_x)
print(avg_y)

red_ball_image.close()
