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
        String represemting the colour
    """
    r, g, b = pixel

    if g > 99 and r < 120 and b < 120:
        return "green"