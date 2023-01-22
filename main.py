from random import randint, random
from joueur import Joueur
from plateau import Plateau
from room import Room

print("JDR - Rube Soulard Gosselin")
#Le joueur choisi la taille du plateau
tailleDuDonjon = int(input("Vous allez pénétrez dans les catacombes de la mort qui tue. Quelle est la taille de ces catacombes selon vous ?"))
monPlateau = Plateau(tailleDuDonjon)

#Debug : utilisé pour afficher toutes les rooms
#print("Plateau MD :")
#monPlateau.printPlateau(False)

#Le joueur choisit le nom de son joueur
nomDuJoueur = input("Vous êtes certainement un aventurier intrépide. Mais quel est votre nom ?")

#permet d'afficher la fiche du joueur
monJoueur = Joueur(nomDuJoueur, randint(1,20), randint(1,20), randint(1,20), 0, 0, 0)

#affiche la fiche du joueur
monJoueur.displayJoueur()

print("Bienvenue " + nomDuJoueur + " !\n Voici la carte des catacombes que tu dois parcourir. Bonne chance !")
monPlateau.printPlateau(True, monJoueur)

#gère le déplacement du joueur dans le donjon
while monJoueur.deplacement(tailleDuDonjon) == True:
    monPlateau.printPlateau(True, monJoueur)
    #condition de sortie
    if monJoueur.getVie() < 1:
        print("Vous êtes mort !")
        break
    if monJoueur.coorx == tailleDuDonjon - 1 and monJoueur.coory == tailleDuDonjon - 1:
        print("Félicitation ! Vous avez trouvé la sortie des catacombes.")
        break
    monJoueur.displayJoueur()


#Afficher une dernière fois les stats du joueur : 
monJoueur.displayJoueur()

print("JDR - Merci d'avoir joué !")