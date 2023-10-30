# Bubble Tea Popularity Algorithm
# Author: Emma
# Date: 27 October 2023

# Ask 5 users what their favourite bubble tea place is 
# Print out a summary of the data

# ------ CONSTANTS

NUM_RESPONDENTS = 5

# ------

# Like counters
coco_likes = 0          # Initialize the variable to 0
suntea_likes = 0
chatime_likes = 0
bubqueen_likes = 0
other_likes = 0

for _ in range(NUM_RESPONDENTS):
    # Ask the user what their favourite place is
    # Store their information somewhere
    print("What's your favourite bubble tea place?")
    fave_place = input().strip(".,!? ").lower()

    # Tally or counting algo
    # If they choose any of the options above, increase the counter
    if fave_place == "coco":
        coco_likes = coco_likes + 1
    elif fave_place == "suntea":
        suntea_likes += 1           # alternative to above
    elif fave_place == "chatime":
        chatime_likes += 1
    elif fave_place == "bubble queen":
        bubqueen_likes += 1
    else:
        other_likes += 1

# Repeat the code above 5 times

# Print out a summary
# Give the raw score AND the percentage
print(f"CoCo Likes: {coco_likes} ({coco_likes/NUM_RESPONDENTS*100}%)")
print(f"Suntea Likes: {suntea_likes} ({suntea_likes/NUM_RESPONDENTS*100}%)")
print(f"Chatime Likes: {chatime_likes} ({chatime_likes/NUM_RESPONDENTS*100}%)")
print(f"Bubble Queen Likes: {bubqueen_likes} ({bubqueen_likes/NUM_RESPONDENTS*100}%)")
print(f"Other Likes: {other_likes} ({other_likes/NUM_RESPONDENTS*100}%)")