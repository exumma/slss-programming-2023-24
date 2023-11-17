# Similar Hobbies
# Emma
# 17 November 2023

similarity_score = 0

# Create two lists for the hobbies of two different people
print("Please enter hobbies, seperated by spaces.")
person_one_hobby = input("Person 1: ")
person_two_hobby = input("Person 2: ")

# Iterate through all movies in first list
for hobby in person_one_hobby.split(" "):
    if hobby in person_two_hobby.split(" "):
        similarity_score += 1

# Display the results
print(f"You have {similarity_score} hobbies in common!")
