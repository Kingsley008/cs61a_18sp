from dice import make_test_dice
from hog import *

def max_scoring_num_rolls(dice=six_sided, num_samples=1000):
    """Return the number of dice (1 to 10) that gives the highest average turn
    score by calling roll_dice with the provided DICE over NUM_SAMPLES times.
    Assume that the dice always return positive outcomes.

    >>> dice = make_test_dice(1, 6)
    >>> max_scoring_num_rolls(dice)
    1
    """
    # BEGIN PROBLEM 9
    "*** YOUR CODE HERE ***"
    num_roll = 1
    averaged_dice = make_averaged(roll_dice, num_samples)
    max_score = 0
    while num_roll <= 10:
        result = averaged_dice(num_roll, dice)
        if result > max_score:
            max_score = result
            this_roll = num_roll
        num_roll = num_roll + 1
    return this_roll
    # END PROBLEM 9

dice = make_test_dice(3)

max_scoring_num_rolls(dice)

print(max_scoring_num_rolls(dice))