# Loop Practice
# Emma 
# 10 October 2023

# Create a list of groceries
groceries = ["hot wheels", "lego", "ice cream", "video games"]

# Do something for each thing in the list
# Print it out in a pretty way
# e.g.
#       * hot wheels
#  ---
#       * lego
#  ---
#       etc.

# print(f"* {groceries[0]}")
# print(f"  ---")
# print(f"* {groceries[1]}")
# print(f"  ---")
# print(f"* {groceries[2]}")
# print(f"  ---")

for item in groceries:
    print(f"* {item}")
    print(f"  ---")

# Using the above method, create the thing below:
# *
# **
# ***
# ****
# *****
# ******

# First create a list
pyramid = ["*","**","***","****","*****","******"]

for row in pyramid:
    print(row)

# Problem:
# Create a New Years Countdown that's automated
# Requirements:
#   - starts at 10
#   - counts down every second printing the second it's at
#   - instead of reaching zero, it prints out "Happy New Year"
# Example Output:
#  10
#  9
#  8
#  ...
#  1
#  Happy New Year!

import time

countdown = ["10", "9", "8", "7", "6", "5", "4", "3", "2", "1", "Happy New Year!"]

for number in countdown:
    print(number)
    time.sleep(1)