from random import randint, random
import re

class Joueur:
    #initialisation
    """
    classe joueur fair un joueur ou une creature qui prend comme paramètre:
        - un nom
        - des points de vie
        - une force
        - des points de chance
        - de l'or
        - sa position x
        -sa position y
    """
    def __init__(self, Name, hp, pc, force, gold, x, y) -> None:
        self.__Name = Name
        self.__hp = hp
        self.__force = force
        self.__pc = pc
        self.__gold = gold
        self.coorx = x
        self.coory = y

    #permet d'afficher la fiche du joueur 
    def displayJoueur(self):
        if self.__hp >= 10:
            print("┌─────────────────────────────────────────┐")
        else:
            print("┌────────────────────────────────────────┐")

        print("│ (҂ಠ ʖ̯ ಠ) :",self.__Name,"│ ❤", self.__hp,"│ ⚔",self.__force,"│ 💲",self.__gold,"│")
        if self.__hp >= 10:
            print("└─────────────────────────────────────────┘")
        else:
            print("└────────────────────────────────────────┘")

    #definit les coordonés x et y du joueur 
    def setCoorJoueur(self, newCoorx, newCoory):
        self.coorx = newCoorx
        self.coory = newCoory
        return True
    
    #premet d'obtenir le nombre d'or du joueur 
    def getGoldJoueur(self):
        return self.__gold

    # permet d'ajouter de l'or au joueur
    def addGoldJoueur(self, goldToAdd):
        self.__gold += goldToAdd
        return True
    
    #permet d'obtenir la vie du joueur 
    def getVie(self):
        return self.__hp
    
    #permet de modifier la vie du joueur
    def setVie(self, newValeurVie):
        self.__hp = newValeurVie
        return True

    #permet d'obtenir la force du joueur
    def getForceJoueur(self):
        return self.__force

    #permet de modifier la vie du joueur 
    def addNourritureJoueur(self, nourritureToAdd):
        self.__hp += nourritureToAdd
        return True

    #permet d'obtenir les caracteristiques du joueur
    def getJoueur(self):
        return self.__Name, self.__hp, self.__force, self.__pc, self.__gold, self.coorx, self.coory
        
    #permet de deplacer le joueur sur le plateau
    def deplacement(self, tailleDuDonjon):
        print("\n Vous êtes dans la salle marquée par (x) - d : droite - q : gauche - z : haut - s : bas | quitter : Mettre fin du jeu")
        print("0 : Cette salle est vide - G : Cette salle contient de l'or - C : Cette salle est habitée par un monstre - N : Cette salle contient de la nourriture")
        direction = input("Entrez une direction: ")
        #droite
        if direction == "d":
            if (self.coorx + 1 == tailleDuDonjon):
                print("Mmmm, il y a un mur ici... Reviens sur ta gauche")
            else:
                self.setCoorJoueur(self.coorx + 1, self.coory)
            return True

            #print(self.coorx, self.coory)
            #self.deplacement()
            #return self.coorx
        #gauche
        elif direction == "q":
            if (self.coorx - 1 == -1):
                print("Mmmm, il y a un mur ici... Reviens sur ta droite")
            else:
                self.setCoorJoueur(self.coorx - 1, self.coory)
            return True

            #print(self.coorx, self.coory)
            #self.deplacement()
            #return self.coorx
        #haut
        elif direction == "z" :
            #Attention, axe y invesré : on enlève pour aller en haut
            if (self.coory - 1 == -1 ):
                print("Mmmm, il y a un mur ici... Redescend.")
            else:
                self.setCoorJoueur(self.coorx, self.coory - 1)
            return True

            #print(self.coorx, self.coory)
            #self.deplacement()
            #return self.coory
        #bas
        elif direction == "s":
            #Attention, axe y invesré : on ajoute pour aller en bas
            if (self.coory + 1 == tailleDuDonjon):
                print("Mmmm, il y a un mur ici... Remonte.")
            else:
                self.setCoorJoueur(self.coorx, self.coory + 1)
            return True
        
        elif direction == "quitter":
            return False

            #print(self.coorx, self.coory)
            #self.deplacement()
            #return self.coory
        #si c'est different de droite, gauche, haut ou bas


        else:
            print("Mmmmm.... Nous n'avons pas compris ce que vous souhaitez faire... Essaiez encore !")
            return True
        
