# Créé par Utilisateur, le 24/04/2021 en Python 3.7

from Comissaire import*
from Jeton import*
from Boss import*
#from Plateau import*



class Prison :

    def __init__ (self,plat,com):

        self.tableau_prison=[0]*5
        self.plateau= plat
        self.commissaire = com
        self.nombre_de_boss = 0

    def ajouter_boss(self):

            position= self.plateau.tableau[self.commissaire.position]
            if isinstance(position,Boss):
                if self.Boss.etat == True :
                    self.tableau_prison[self.nombre_de_boss] = jeton
                    self.nombre_de_boss += 1

                    if self.nombre_de_boss==5:
                        print("il y a 5 boss en prison, il n'y a plus de place en prison => la partie est terminée")
                    else:
                        print("la partie n'est pas encore terminée")
            print(self.tableau_prison)


    def retourner_les_jetons (self):

        for i in range (self.nombre_de_boss): #Parcours des jetons de la prison
            num_couleur = self.tableau_prison[i].getCouleur()
            for i in range (len(self.plateau.tableau[i])): #Parcours le plateau
                if num_couleur == self.jeton.num_coul:
                    self.jeton.etat=True
            for i in range(len(self.joueur.tabj[i])): #Parcours les jetons des joueurs
                if num_couleur == self.jeton.num_coul:
                    self.jeton.etat=True
