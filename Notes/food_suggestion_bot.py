# Title: Food Suggestion Bot
# Author: Emma
# 6 October 2023

# A bot that asks the user what their favourite food is. Based on that food,
# it will classify the type/genre/cuisine of the food, then give a restaurant suggestion

import random
import time

# Introduce the bot to the user
# Ask the user what their favourite food is
print("Hello, I am here to suggest you a restaurant.")
time.sleep(1)
fave_food = input("To help me suggest a restaurant, tell me what your favourite food is. ")
time.sleep(1)

# Italian Cuisine
italian_food = ["pasta", "pizza", "canneloni", "tiramisu"]

# Add another cuisine that our bot should make a sugestion for
# Japanese Cuisine
japanese_food = ["sushi", "tonkatsu" "bento box", "teriyaki", "tempura", "ramen", "gyoza"," takoyaki"]

# Chinese Cuisine
chinese_food = ["hot pot", "fried rice", "mapo tofu", "dumplings", "steamed bun", "egg drop soup"]

# If they answer with Italian food, suggest an Italian restaurant
if fave_food.lower().strip("!.,?") in italian_food:
        print("I see that you might like Italian food. 🍕")
        time.sleep(1)
        print("I suggest Broli Kitchen.")
        time.sleep(1)
        print("Here's their address.")
        print("186-8180 No 2 Rd, Richmond, BC V7C 5K1")
#If they answer with Japanese food, suggest a Japanese restaurant
elif fave_food.lower().strip("!.,?") in japanese_food:
    print("I see that you like Japanese food. 🍱")
    time.sleep(1)
    print("I suggest Otaru Japanese kitchen")
    time.sleep(1)
    print("Here's their address.")
    print("8180 No 2 Rd #168, Richmond, BC V7C 5K1")
elif fave_food.lower().strip("!.,-?") in chinese_food:
     print("I see that you might like Chinese food.")
     time.sleep(1)
     print("I suggest Shanghai River Restaurant.")
     time.sleep(1)
     print("Here's there address.")
     print("7831 Westminster Hwy, Richmond, BC V6X 4J4")
else:
    print("Sorry, I'm not sure what kind of food that is.")
    time.sleep(1)
    print("I can't unfortunately, provide a suggestion.")