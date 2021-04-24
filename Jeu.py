# Créé par Utilisateur, le 24/04/2021 en Python 3.7

from Gangster import*
from Argent import*
from Joueur import*
from Plateau import*
from Comissaire import*
from Prison import*
import random





class Jeu:





    def __init__ (self):
        nb_joueur=0
        #self.nb_joueur
        self.tab = []
        self.plat = Plateau()
        self.com=Comissaire()
        self.prison=Prison(self.plat,self.com)
        self.joueur=Joueur(self,self.com)
        self.joueur_courant=0
        self.relie_commissaire_plateau(self.com,self.plat)
        self.relie_prison_plateau(self.plat,self.prison)
        self.nom_des_joueurs()





    def relie_commissaire_plateau(self,com,plat):
        self.plat.commissaire=self.com
        self.com.plateau=self.plat



    def relie_prison_plateau(self,plat,prison):
        self.plat.prison=self.prison
        self.prison.plateau=self.plat




    def nom_des_joueurs(self):



        x=0
        while x==0:



            self.nb_joueur = input ("Combien y a t'il de joueurs ? ")



            try:
                int(self.nb_joueur)



                while int(self.nb_joueur)<2 or int(self.nb_joueur)>5 :
                    self.nb_joueur = int (input ("Il faut 2 à 5 joueurs pour jouer "))



                for i in range (int(self.nb_joueur)):
                    i  =  (input ("Quel est votre pseudo ? "))
                    self.tab=Joueur(i,self.com)
                x=1



            except ValueError:
                x=0



    def tirage_aleatoire(self):
        self.joueur_courant=random.randint(1,int(self.nb_joueur))
        print ("A toi de jouer: Joueur numéro", self.joueur_courant)






    def joueur_suivant (self):



        while self.prison.nombre_de_boss!=5:
            self.joueur_courant=self.joueur_courant +1
            if self.joueur_courant==self.nb_joueur:
                self.joueur_courant=0
            self.joueur.jouer()
            self.plat.affichage(self.com)
        print ("Le jeu est terminé")





    def creation_des_joueurs(self,p):
        self.tab = [0]*self.nb_joueur
        for i in range (self.nb_joueur):
            self.tab[i]= Joueur(p)






    def comptage_point_de_chaque_joueurs(self):



        score = [0]



        for i in range (self.nb_joueur):



            scorej = self.joueur.comptage_point()
            score[self.joueur_suivant] = scorej
            print("Joueur " + str(self.joueur_suivant) + " a fait un score de " + str(scorej))




        m = max(score.items(), key=operator.itemgetter(1))[0]
        print("C'est donc le Joueur " + str(m) + " qui a gagné !")




    def partie(self):
            self.plat.affichage(self.com)
            self.tab.jouer()



           #self.comptage_point_de_chaque_joueurs()
            print(" ")




S=Jeu()
S.partie()
S.joueur_suivant()
