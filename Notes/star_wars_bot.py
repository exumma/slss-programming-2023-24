# Star Wars Bot
# Emma
# 16 October 2023

import time

# Introduce yourself
print("Hi, I am a Star Wars bot!")
time.sleep(1)

# Tell them that you will decide if the can join the Dark Side
print("I will decide if you can join the Dark Side.")
time.sleep(1)

# Ask if red is their favourite colour
colour_red = input("Is red your favourite colour? ")

# Ask if they like capes
likes_capes = input("Do you like capes?")

# If yes to one of them or both, they are in the Dark Side
# Respond with Dark side it is!
# If no to both, they are in the Light Side
# Respond with Light side I see.

if colour_red.lower().strip(".,!?") == "yes" or likes_capes.lower().strip(".,?!") == "yes":
    print("Dark side it is!")
else:
    print("Light side, I see.")


