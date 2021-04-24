# Créé par Utilisateur, le 24/04/2021 en Python 3.7

from Gangster import *
from Argent import *
from Boss import*
from random import shuffle
from random import*
#import Comissaire

class Plateau:
    def __init__(self):

        self.commissaire=None
        self.tableau=[0]*42

        for i in range (7):

                g = Gangster (  1,i)    ### 1 tetes
                self.tableau[6*i+0] = g
                g = Gangster (2,i )   ### 2 tetes
                self.tableau[6*i+1] = g
                g = Gangster ( 2,i )    ### 2 tetes
                self.tableau[6*i+2] = g
                g = Gangster ( 3,i )   ### 3 tetes
                self.tableau[6*i+5] = g
                a= Argent(i)
                self.tableau[6*i+3] = a
                b= Boss (i)
                self.tableau[6*i+4] = b

        self.aleatoire()

    def aleatoire(self):
       shuffle(self.tableau)

    def affichage ( self, commissaire ) :
        print(" ")
        for i in range(len(self.tableau)):
            if self.tableau[i]!=None:

                self.tableau[i].afficher()

                if i==self.commissaire.position:
                    print(self.commissaire.position)
                    print("C")

from random import*

class Comissaire:
    def __init__(self):
        self.position= 0
        self.plateau = None

    def choix_de_deplacement(self):

        a=randint(2,4)
        if a==2:
            x=0
            while x==0:

                D=(input("Vous voulez avancer de 1 ou 2? "))
                try:
                    int(D)
                    if D==1:
                        self.position=self.position+1
                    elif D==2:
                        self.position=self.position+2
                        print(self.position )
                    elif int(D)<1 or int(D)>2:
                        D=int(input("Vous ne pouvez avancer que de 1 ou 2."))
                    x=1

                except ValueError:
                    x=0

        elif a==3:
            x=0
            while x==0:
                D=(input("Vous voulez avancer de 1, 2 ou 3 ?"))

                try:
                    int(D)
                    if D==1:
                        self.position=self.position+1
                    elif D==2:
                        self.position=self.position+2
                    elif D==3:
                        self.position=self.position+3
                    elif int(D)<1 or int(D)>3:
                        D=int(input("Vous ne pouvez avancer que de 1, 2 ou 3."))
                    x=1

                except ValueError:
                    x=0

        elif a==4:

            x=0

            while x==0:

                D=(input("Vous voulez avancer de 1, 2, 3 ou 4 ?"))

                try:
                    int(D)

                    if D==1:
                        self.position=self.position+1
                    elif D==2:
                        self.position=self.position+2
                    elif D==3:
                        self.position=self.position+3
                    elif D==4:
                        self.position=self.position+4
                    elif int(D)<1 or int(D)>4:
                        D=int(input("Vous ne pouvez avancer que de 1, 2, 3 ou 4."))
                    x=1

                except ValueError:
                    x=0

        if self.plateau.tableau[self.position] == None :
            a=0
            for i in range (0, self.position):
                if self.plateau.tableau[i]==None :
                    a= a+1
            self.position = a


    def enlever_le_jeton(self):

        jeton = self.plateau.tableau[self.position]

        for i in range (self.position, len(self.plateau.tableau)-1):
            self.plateau.tableau[i]=self.plateau.tableau[i+1]
            self.plateau.tableau[41]=None

        if isinstance ( jeton, Boss ) :
            jeton.allerEnPrison()
        else :
            return jeton