# Parental Bot
# Emma
# 17 November 2023

score = 0

# Create a bot and ask questions
questions = [
    "Did you eat?",
    "Did you study?",
    "Did you do your laundry?",
    "Did you call grandma?"
]

for question in questions:
    answer = input(question)
    if answer.lower().strip(".,?!") == "yes":
        score +=1

if score <= 0:
    print("I'm coming over")
elif score <= 2:
    print("Ok.")
else:
    print("Good!")



