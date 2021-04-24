# Créé par Utilisateur, le 24/04/2021 en Python 3.7

from Jeton import *



class Gangster(Jeton):
    def __init__(self, nb,c):
        self.nombre_de_tete=nb
        self.num_coul=c
        self.etat=False




    def comptage_point(self):
        if self.etat ==False:
            score=self.nombre_de_tete
            return score



        else:
            score=-self.nombre_de_tete
            return score



    def afficher(self):
        print("Gangster",self.getCouleur(),self.nombre_de_tete)

