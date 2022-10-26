"""Direction cell class."""
from Cell import Cell


class DirectionCell(Cell):

    def __init__(self, x, y, xt, yt):
        self._x = x
        self._y = y
        self._treasureX = xt
        self._treasureY = yt
        self._isVisited = False

    def visit(self):

        # On check dans quel direction le coffre se trouve, il peut donc se trouver selon deux direction (haut/bas) par rapport a x (ligne) et (droite/gauche) par rapport a y (colonne)
        print("-------------")
        print("| Direction |")
        print("-------------")
        res=""
        if self._x < self._treasureX:
            res= res+ "en bas "
        elif self._x > self._treasureX:
            res= res+"en haut "
        if self._y > self._treasureY:
            res= res+"à gauche"
        elif self._y < self._treasureY:
            res= res+"à droite"
        print("Le coffre se trouve "+res)

        if self._x == self._treasureX and self._y == self._treasureY:
            self._isVisited = True
            return True
        else :
            self._isVisited = True
            return False
