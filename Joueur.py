# Créé par Utilisateur, le 24/04/2021 en Python 3.7

from Gangster import*
from Argent import*
from Plateau import*
from Comissaire import*
from Jeton import*
from Prison import*



class Joueur:



    def __init__ (self, p,com):
        self.prenom = p
        self.nb_jeton = 0
        self.commissaire=com
        self.tabj = [0]*40





    def jouer(self):



            self.commissaire.choix_de_deplacement()
            jeton = self.commissaire.enlever_le_jeton()



            if isinstance ( jeton, Jeton ) :
                self.tabj[self.nb_jeton] = jeton
                self.nb_jeton += 1




    def comptage_point (self):
        somme1 = 0
        somme2=0
        for i in range(len(self.tabj)):
            jeton=self.tabj[i]
            if isinstance ( jeton, Gangster) :
                 somme1=somme1 + jeton.comptage_point()



            elif isinstance ( jeton, Argent) :
                 somme2=somme2 + jeton.comptage_point()



        somme =somme1+somme2
        return somme
