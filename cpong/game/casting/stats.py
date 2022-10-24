from constants import *
from game.casting.actor import Actor


class Stats(Actor):
    """The game stats."""

    def __init__(self, debug = False):
        """Constructs a new Stats."""
        super().__init__(debug)
        self._level = 1
        self._volleys = 0

    def add_volley(self, points):
        """Adds the given points to the score.
        
        Args:
            points: A number representing the points to add.
        """
        self._volleys += points

    def get_level(self):
        """Gets the level.

        Returns:
            A number representing the level.
        """
        return self._level

  
    def get_volleys(self):
        """Gets the score.

        Returns:
            A number representing the score.
        """
        return self._volleys

    
    def next_level(self):
        """Adds one level."""
        self._level += 1

    def reset(self):
        """Resets the stats back to their default values."""
        self._level = 1
        self._score = 0