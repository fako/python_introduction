"""
A script to play around with Python a bite
To setup run:
conda create --name pi
pip install -r requirements.txt
"""
from pprint import pprint
import pandas as pd  # data analysis library

from tamagotchi import KillerRabbit


if __name__ == "__main__":

    # Creating some rabbits!
    snuggles = KillerRabbit("Snuggles")
    winky = KillerRabbit("Winky", hunger=100)
    problem_child = snuggles + winky

    # In ipython:
    # See what a KillerRabbit is with KillerRabbit?
    # And what a KillerRabbit can do with KillerRabbit.

    # We're making some dinner :P
    food = ["a knight", "a priest", "a charlatan"]
    snuggles_dinner, winky_lunch, child_dessert = food  # tuple unpacking

    # Go ahead and feed a KillerRabbit. Check out KillerRabbit.feed. in ipython

    # Managing our population
    rabbits = [
        snuggles, winky, problem_child, snuggles, winky  # oops some duplicates!
    ]
    # correcting the duplicates with list slicing
    rabbits = rabbits[1:-1]
    # list comprehensions in action to get only happy rabbits
    happy_rabbits = [
        rabbit for rabbit in rabbits if rabbit.happiness > 30
    ]
    happy_rabbits.sort(
        key=lambda rabbit: rabbit.happiness,  # lambda's are simple anonymous functions
        reverse=True
    )
    happy_rabbit_names = [str(rabbit) for rabbit in happy_rabbits]
    happy_rabbits_hall_of_fame = ", ".join(happy_rabbit_names)

    # Keep track of the population with data!
    rabbit_records = [rabbit.to_record() for rabbit in rabbits]  # pprint this!
    population = pd.DataFrame.from_records(rabbit_records)

    # A DataFrame is a matrix containing data
    # You can make our population very happy with
    # 1)   population["happiness"] *= 2
    # 2)   population["hunger"] /= 2
    # Or try some real science:
    # population["satisfaction_coefficient"] = \
    #   population["happiness"] / population["hunger"]

    # When in doubt what to do
    # import this
