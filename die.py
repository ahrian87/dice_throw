from random import randint


class Die():
    """Class illustrating a single game die"""

    def __init__(self, num_sides=6):
        """Standard game die - 6 sides"""
        self.num_sides = num_sides

    def roll(self):
        """Random number in range from 1 to the number of sides"""
        return randint(1, self.num_sides)
