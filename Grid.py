"""Grid class."""
from DirectionCell import DirectionCell
from DistanceCell import DistanceCell
from TreasureCell import TreasureCell
from Player import Player
import random


class Grid:
    """Define a grid."""

    def __init__(self, size):
        """Initialize the grid."""
        self.__size = size
        self.__player = Player()
        self.__grid = [[0]*self.__size for x in range(0, self.__size)]

    def __initializeCells(self):
        """Initialize each cell of the grid."""

        xt = random.randint(0,19)
        yt = random.randint(0,19)

        for x in range(0, self.__size) :
            for y in range(0, self.__size) :
                rand = random.randint(0,4)
                if x==xt and y==yt : self.__grid[x][y] = TreasureCell(xt, yt)
                elif rand==0 : self.__grid[x][y] = DistanceCell(x, y, xt, yt)
                else : self.__grid[x][y] = DirectionCell(x, y, xt, yt)



    def __display(self):
        """Display the grid."""
        print("-----------------")
        print("| Grille de jeu |")
        print("-----------------")

        for x in range(0, self.__size) :
            for y in range(0, self.__size) :
                self.__grid[x][y].display()
            print('  \n', end='') # Retour a la ligne apres le parcour d'une ligne entiere

    """
        Dans notre Jeu, nous avons X qui correspond au ligne de notre tableau et Y qui correspond aux colonnes de notre tableau.     
    """

    def launch(self):
        """Launch the game."""
        # Initialize grid and player.
        self.__initializeCells()
        self.__player.askName()

        gameEnd = False
        while not gameEnd:
            # Display the grid.
            self.__display()

            # Ask the column and line.
            x = self.__player.askXOrY('Entrez la prochaine ligne a jouer > ',
                                      self.__size)
            y = self.__player.askXOrY('Entrez la prochaine colonne a jouer > ',
                                      self.__size)
            if self.__grid[x][y].isVisited():
                print('La case est déjà jouée.')
            else:
                gameEnd = self.__grid[x][y].visit()
        print('Bravo ' + self.__player.getName() + ' vous avez gagné.')
