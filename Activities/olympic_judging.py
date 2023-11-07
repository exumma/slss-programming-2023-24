# Olympic Judging
# Emma Xu
# 1 November 2023

# List out the current scores from each judge
judge_one = 0
judge_two = 0
judge_three = 0
judge_four = 0
judge_five = 0 

# Store their responses
# Ask the questions to the user
rating_1 = int(input("Rate the performance from a scale of 1 to 10. ").strip(".,?! "))
judge_one += rating_1

rating_2 = int(input("Rate the performance from a scale of 1 to 10. ").strip(".,?! "))
judge_two += rating_2

rating_3 = int(input("Rate the performance from a scale of 1 to 10. ").strip(".,?! "))
judge_three += rating_3

rating_4 = int(input("Rate the performance from a scale of 1 to 10. ").strip(".,?! "))
judge_four += rating_4

rating_5 = int(input("Rate the performance from a scale of 1 to 10. ").strip(".,?! "))
judge_five += rating_5

# Calculate the average
average = (judge_one + judge_two + judge_three + judge_four + judge_five)/ 5

# Print out the scores and average
print(f"Judge 1: {judge_one}")
print(f"Judge 2: {judge_two}")
print(f"Judge 3: {judge_three}")
print(f"Judge 4: {judge_four}")
print(f"Judge 5: {judge_five}")
print(f"Your Olympic score is {average}")
