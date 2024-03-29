# Colour Helper
# Emma
# 13 December 2023

# Do you need help with colours?
# This is for you!

def pixel_to_string(pixel: tuple) -> list:
    """Take a rgb 3-tuple and "interpret it" as a colour and return that colour's name 
    
    Params:
        pixel - 3-tuple of (red, green, blue)

    Return:
        String representing the colour
    """
    r, g, b = pixel

    if g > 95 and r < 120 and b < 120:
        return "green"
    if g < 25 and b < 25 and r > 150:
        return "red"
    if g < 100 and b < 100 and r > 155:
        return "ball red"
    if g <= 95 and b >= 95 and r <= 95:
        return "blue"
    
print(pixel_to_string((160, 0, 4))) #red

def is_light(pixel: tuple) -> bool:
    """Take a rgb 3-tuple and "interpret" it as a colour
    
    Params:
        pixel - 3-tuple of (red, green and blue)

    Return:
    If the average of the tuple values is greater than or equal to 128, it returns true.
    If less than 128, it returns false.
    """

    r, g, b = pixel

    if sum(pixel)/len(pixel) >= 128:
        return True
    else:
        return False

black_pixel = (0, 0, 0)
dark_gray_pixel = (127, 127, 127)
light_gray_pixel = (128, 128, 128)
white_pixel = (255, 255, 255)

(is_light(black_pixel))            # False
(is_light(dark_gray_pixel))        # False
(is_light(light_gray_pixel))       # True
(is_light(white_pixel))            # True

from PIL import Image

with Image.open("./Images/best_pizza.jpg") as im:

    # store the height and width of the image
    image_height = im.height
    image_width = im.width

    white_pixel = (255, 255, 255)
    black_pixel = (0, 0, 0)

    for y in range(image_height):
        for x in range(image_width):
            pixel = im.getpixel((x, y))
            # check pixel if it's white
            if is_light(pixel) == True:
                # replace it with a white pixel 
                im.putpixel((x, y), white_pixel)
            else:
                im.putpixel((x, y), black_pixel)

    # save the image
    im.save("./Images/result.jpg")

def pixel_to_grayscale(pixel: tuple) -> tuple:
    """Returns a grayscale version of the given pixel"""

    gray = int(pixel[0] * 0.3 + pixel[1] * 0.59 + pixel[2] * 0.11)
 
    return (gray, gray, gray)

def iamge_to_grayscale(filename: str) -> None:
    """Convert an image to grayscale"""

    with Image.open(f"./Images/{filename}") as im:
        for y in range(image_height):
            for x in range(image_width):
                pixel = im.getpixel((x, y))
                # check pixel if it's white
                if is_light(pixel) == True:
                    # replace it with a white pixel 
                    im.putpixel((x, y), white_pixel)
                else:
                    im.putpixel((x, y), black_pixel)