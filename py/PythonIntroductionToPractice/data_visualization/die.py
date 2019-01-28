from random import randint

class Die():
    """a class represent a dice"""

    def __init__(self, num_sides=6):
        """dice's default plane is 6"""
        self.num_sides = num_sides

    def roll(self):
        """return a random value from 1 to the number of dice'plane"""
        return randint(1, self.num_sides)
