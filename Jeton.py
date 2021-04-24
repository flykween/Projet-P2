# Créé par Utilisateur, le 24/04/2021 en Python 3.7

   ####        Jetons          ####




tab_couleur=["rouge","violet","orange","bleu","vert","marron","jaune"]



class Jeton :



    def __init__ (self, c,nb) :
        self.num_coul=c
        self.etat = False




    def getCouleur(self):
        return tab_couleur[self.num_coul]





    def sens(self) :
        if self.etat == False :
            return False
        else :
            return True



    def retourner():
        self.etat = True
