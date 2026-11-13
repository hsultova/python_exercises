from random import randint

class Die:
    """Represent a single die."""

    def __init__(self, num_sides=6) -> None:
        """Default is a six-sided die."""
        self.num_sides = num_sides

    def roll(self):
        """Return a random value between 1 and number of sides."""
        return randint(1 , self.num_sides)