# Créé par Utilisateur, le 24/04/2021 en Python 3.7

from Jeton import*



class Argent (Jeton):



    def __init__(self,c):
        self.num_coul=c
        self.etat=False





    def comptage_point(self) :



        if self.etat==False:
            score=3
        else:
            score=0



        return score




    def afficher(self):
        print("Argent", self.getCouleur())
