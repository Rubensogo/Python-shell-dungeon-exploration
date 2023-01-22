
from random import randint, random
from room import Room
from joueur import Joueur

class Plateau:
    """
    Definit un plateau qui prend en paramètre;
    -une taille 
    la position en haut à gauche est 0 et l'axe y qui devrait être négatif en descendant vers le bas, cependant il augmente.
    """
    def __init__(self, sizePlateau):
        self.__sizePlateau = sizePlateau
        self.matrixPlateau = [[0] * self.__sizePlateau for i in range(self.__sizePlateau)]
        for row in range(self.__sizePlateau):
            for col in range(self.__sizePlateau):
                self.matrixPlateau[row][col] = Room(0, row, col)

    #permert d'afficher le plateau
    def printPlateau(self, versionForPlayer, currentJoueur):
        #Première ligne :
        print ("-" * 7 * self.__sizePlateau)
        for row in range(self.__sizePlateau):
            ligne = ""
            for col in range(self.__sizePlateau): 
                lastCol = self.__sizePlateau-1
                if (col == 0) :
                    ligne = ligne + "| " + self.matrixPlateau[row][col].getTypeRoom(versionForPlayer, currentJoueur) + "  "
                elif (col == lastCol) :        
                    ligne = ligne + "  " + self.matrixPlateau[row][col].getTypeRoom(versionForPlayer, currentJoueur) + " |"
                else :
                    ligne = ligne + "  " + self.matrixPlateau[row][col].getTypeRoom(versionForPlayer, currentJoueur) + "  "
                #print ("row " + str(row) + " col " + str(col) + " val " + self.matrixPlateau[row][col].getTypeRoom())
            print (ligne)
        #Dernière ligne :
        print ("-" * 7 * self.__sizePlateau)
        #for row in self.matrixPlateau:
        #    print(row.getTypeRoom())

    #permet de savoir la room sur laquelle le joueur se trouve
    def getRoomFromPlateau(self, row, col):
        print("Room :")
        print (self.matrixPlateau[row][col].getTypeRoom())
    
    #permet de marquer la room commme étant visitée, donc de faire disparaitre le * et de mettre une lettre à la place
    def setRoomAsVisitedFromPlateau(self, row, col):
        self.matrixPlateau[row][col].setRoomAsVisited()