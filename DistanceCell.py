"""Distance cell class."""
import math

from Cell import Cell


class DistanceCell(Cell):

    def __init__(self,x, y, xt, yt) :
        self._x = x
        self._y = y
        self._treasureX = xt
        self._treasureY = yt
        self._isVisited = False

    def visit(self):

        print("-------------")
        print("| Distance |")
        print("-------------")
        # On calcule la distance de la case actuelle par rapport au tresor.
        res = math.sqrt(math.pow(self._treasureX-self._x,2) + math.pow(self._treasureY-self._y, 2))
        print("Le coffre se trouve a une distance d'environ "+str((int)(res))+" cases.") # on affiche la distance
        # le resultat est ici arrondi comme demandé dans l'ennoncé

        if self._x == self._treasureX and self._y == self._treasureY:
            self._isVisited = True
            return True
        else :
            self._isVisited = True
            return False

