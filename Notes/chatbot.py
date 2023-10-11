# Chatbot
# Author: Emma
# Date: 20 September 2023

import random
import time

# Greet the user
print("Hello there! 🤖")
time.sleep(1.5)
print("I'm a crude Chatbot, here to talk to you.")
time.sleep(1.5)


# Get the user's name and store it in a variable 
user_name = input("So... What's your name? ")
time.sleep(1.5)

# Respond with the user's name in a friendly way
print(f"It's good to meet you {user_name}.")
time.sleep(1.5)

# Ask the user what their favourite food is
favourite_food = input("What's your favourite food? ")
time.sleep(1.5)

# If their favourite food is sushi, reply with yum.
if favourite_food == "sushi":
    print("Yum! 🍣")
    print("I think I love sushi!")
elif favourite_food == "burgers" or favourite_food == "Burgers":
    print("🍔")
    print("Burgers, I hear they are delicious.")
else:
    # Create a list of possible responses 
    list_of_food_responses = [
        f"Oh. I've never had {favourite_food} before.", 
        "MMmmmmm. That sounds good!",
        "I heard that that is delicious.",
        "Cool."
    ]

    # Choose one of those reponses randomly
    random_food_response = random.choice(list_of_food_responses)

# Print out that chosen response
print(random_food_response)