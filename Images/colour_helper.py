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

    if g > 99 and r < 120 and b < 120:
        return "green"
    
def is_light(pixel: tuple) -> bool:
    """Take a rgb 3-tuple and "interpret" it as a colour
    
    Params:
        pixel - 3-tuple of (red, green and blue)

    Return:
    If the average of the tuple values is greater than or equal to 128, it returns true.
    If less than 128, it returns false.
    """

    r, g, b = pixel

    if (r + g + b)/3 >= 128:
        return True
    else:
        return False

black_pixel = (0, 0, 0)
dark_gray_pixel = (127, 127, 127)
light_gray_pixel = (128, 128, 128)
white_pixel = (255, 255, 255)

print(is_light(black_pixel))            # False
print(is_light(dark_gray_pixel))        # False
print(is_light(light_gray_pixel))       # True
print(is_light(white_pixel))            # True