# Créé par Utilisateur, le 24/04/2021 en Python 3.7

  ####            BOSS            ####



from Jeton import *



class Boss(Jeton):
    def __init__ (self,c):
        self.etat=False
        self.num_coul=c



    #def comptage_point(self):
      #  if self.etat == False :
     #       score



    def allerEnPrison(self) :
        self.etat = True



    def estEnPrison (self):
        if self.etat== True :
            return True
        else :
            return False



    def afficher(self):
        print("Boss",self.getCouleur())
