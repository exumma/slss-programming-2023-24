# Semester Evaluator Bot
# Emma
# 6 November 2023

number_of_courses = int(input("How many courses are you taking?"))

total_score = 0

for i in range(number_of_courses):
    rating = int(input(f"How would you rate course {i+1} out of 5? "))
    total_score += rating

average = total_score / number_of_courses

if total_score <= 1:
    print(f"{average}? Ouch.")
elif total_score <3:
    print(f"{average}? Not a bad semester.")
else:
    print(f"{average}? Glad to hear that!")

