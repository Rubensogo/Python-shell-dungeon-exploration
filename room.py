from random import randint, random
from joueur import Joueur

class Room:
    """
    defifnit une classe Room qui prend comme paramètre :
    - un type de room (nourriture, or , créature ou rien du tout)
    - une coordonnée x
    - une coordonnée y
    """
    def __init__ (self, typeRoom, coory, coorx ):
        self.__typeRoom = typeRoom
        self.__coorx = coorx
        self.__coory = coory
        self.__isVisited = False; 
        randomCounter = randint(0,99)
        """met en place les chances d'apparition des chaques type de salle"""
        if randomCounter < 40:
            self.__typeRoom = "O"
        elif randomCounter <= 65:
            self.__typeRoom = "G"
        elif randomCounter <= 80 :
            self.__typeRoom = "C"
        elif randomCounter <= 99:
            self.__typeRoom = "N"

    #permet de faire un event sur le joueur en fonctiuon de la type de room
    def getTypeRoom(self, versionForPlayer, currentJoueur):
        #version du MD
        if (versionForPlayer == False):
            if currentJoueur.coorx == self.__coorx and currentJoueur.coory == self.__coory:
                self.setRoomAsVisited()
                #event trouver de l'or
                if self.__typeRoom == "G":
                    currentJoueur.addGoldJoueur(randint(1,100))
                #event trouver de la nourriture
                if self.__typeRoom == "N":
                    currentJoueur.addNourritureJoueur(randint(1,3))
                return ("(" + self.__typeRoom + ")")
            else :
                return (" " + self.__typeRoom + " ")
        else:
            #version du joueur
            if currentJoueur.coorx == self.__coorx and currentJoueur.coory == self.__coory:
                self.setRoomAsVisited()
                #event trouver de l'or
                if self.__typeRoom == "G":
                    currentJoueur.addGoldJoueur(randint(1,100))
                #event trouver de la nourriture
                if self.__typeRoom == "N":
                    currentJoueur.addNourritureJoueur(randint(1,3))
                #event trouver une créature
                if self.__typeRoom == "C":
                    randomCreature = randint(0,4)
                    listeCreature = ["goblin", "troll", "warg", "zombie", "squelette"]
                    #Les créatures n'ont pas de chance, mais de l'or
                    newCreature = Joueur(listeCreature[randomCreature], randint(1,20), randint(1,20), randint(5,15), randint(20,100), self.__coorx, self.__coory)
                    #A améliorer : pour l'instant je compare les pv à la force, si le joueur est encore vivant à l'issu d'un tour, on considère qu'il a gagné.
                    newValeurVieJoueur = currentJoueur.getVie() - newCreature.getForceJoueur()
                    currentJoueur.setVie(newValeurVieJoueur)
                    if currentJoueur.getVie() > 0:
                        #Le joueur gagne l'or de la créature
                        currentJoueur.addGoldJoueur(newCreature.getGoldJoueur())
                        return ("(!)")
                    else:
                        return ("(+)")

                return ("(" + self.__typeRoom + ")")
            if (self.__isVisited == True):
                return (" " + self.__typeRoom + " ")
            else:
                return " * "
                #return self.__typeRoom + str(self.__coorx) + str(self.__coory)
    
    # permet d'afficher toute les info d'une room sur le plateau (debug)
    def getFullInfoRoom(self):
        return str(self.__typeRoom) + "-" + str(self.__coorx) + ":" + str(self.__coory)

    #permet de marquée la room comme étant visitée
    def setRoomAsVisited(self):
        self.__isVisited = True
        return True