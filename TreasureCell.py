"""Treasure cell class."""
from Cell import Cell

class TreasureCell(Cell) :

    def __init__(self, xt, yt) :
        #Ici la position x/y est la position du tresor, il n'est donc pas necessaire de mettre x et y en paramètre
        self._x = xt
        self._y = yt
        self._treasureX = xt
        self._treasureY = yt
        self._isVisited = False

    def visit(self):
        # On verifie que la case est la case ou le coffre se situe (vrai)
        if self._x == self._treasureX and self._y == self._treasureY:
            self._isVisited = True
            return True
        else :
            self._isVisited = True
            return False
