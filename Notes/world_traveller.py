# World Traveller Bot
# Emma Xu
# 3 November 2023

# Ask the user's name and greet them
user_name = input("What's your name? ")
print(f"Hello, {user_name}! It's nice to meet you!")

# Ask the user if they have been to each of the continenets
# Create a list of questions to ask
questions = [
    "Have you been to Asia?",
    "Have you been to Europe?", 
    "Have you been to North America?",
    "Have you been to South America?",
    "Have you been to Australia?",
    "Have you been to Africa?",
    "Have you been to Antarctica?"
]

continents_score = 0

# Ask the questions to the user
for question in questions:
    print(question)
    user_response = input()

    if user_response.lower().strip(".,?!") in ["yes", "yeah", "ye", "yea", "yup", "yups"]:
        continents_score = continents_score+ 1
    else:
        continents_score + 0

# Tell the user how many continents the've been to
print(f"I see, you've visited {continents_score}/7 continents!")
