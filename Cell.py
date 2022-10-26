"""Cell class."""

from abc import ABC, abstractmethod


class Cell(ABC):
    """Abstract class to define a cell."""

    def __init__(self, x, y, treasureX, treasureY):
        """Initialize the cell with position values."""
        self._x = x
        self._y = y
        self._treasureX = treasureX
        self._treasureY = treasureY
        self._isVisited = False

    def display(self):
        """Display a cell."""
        if self._isVisited:
            print('  ', end='')
        else:
            print('x ', end='')

    @abstractmethod
    def visit(self):

        if self._x == self._treasureX and self._y == self._treasureY:
            self._isVisited = True
            return True
        else :
            self._isVisited = True
            return False



    def isVisited(self):
        """Getter for isVisited."""
        return self._isVisited

