# Winter Holidays
# Emma Xu
# 8 January 2024

import random

# Requirements:
# - create a function calledf winter_holiday()
    # - takes one parameter - string
    # - returns a summary of an event from your holidays

def winter_holiday(good_or_bad: str) -> str:
    """Give a summary of our winter holidays 2023/24
    
    Params:
        good_or_bad - string that indicates whether the event is good or bad
    
    Returns:
        an event that happened to you during the holidays 
        the event is selected part
    """
    
    # Make a list of the good and bad events
    good = [
        "I met up with a lot of family friends",
        "I was able to sleep a lot",
        "I ate a lot of hotpot",
        "I finished watching 3 different shows"
    ]

    bad = [
        "I had to complete my math homework and work on a presentation",
        "I still woke up at 9:30am even though I planend to wake up at 11am",
        "It was really cold"
    ]
    
    if good_or_bad.lower().strip(".,?!") == "good":
        return print((random.choice(good)))
    else:
        return print(random.choice(bad))
    
def main() -> None:
    # Runs all the things we want to test in our .py file
    winter_holiday("good")
    winter_holiday("bad")

if __name__ == "__main__":
    main()