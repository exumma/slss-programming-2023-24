# McDoland's Program
# Emma Xu
# 3 November 2023

burger = 0
fries = 0

# Ask the user if the would like a burger for $5 (yes/no)
burger_choice = input("Would you like a burger for $5? (Yes/No)")
if burger_choice.lower().strip(".,?!") == "yes":
    burger_cost = burger + 5
else:
    burger_cost = burger

# Ask if the user would like fries for $3 (yes/no)
fries_choice = input("Would you like fries for $3? (Yes/No)")
if fries_choice.lower().strip(".,?!") == "yes":
    fries_cost = fries + 3
else:
    fries_cost = fries

# Calculate the total include 14% tax
total = (fries_cost + burger_cost)*1.14

# Print out the total
print(f"Your total is ${total}")