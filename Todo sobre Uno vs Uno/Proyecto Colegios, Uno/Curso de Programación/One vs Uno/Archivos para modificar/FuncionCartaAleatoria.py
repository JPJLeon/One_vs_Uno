#Creado por:    Juan Pablo Leon 
#               Yeison Fernandez
#               Jordan Esquivel

from random import *

def carta_aleatoria(mano,mazo): #Se roba una carta al azar del mazo,
        carta=choice(mazo)      #removiendola del mazo y agregandola
        mano.append(carta)      #a la mano que se especifico
        mazo.remove(carta)
        return mano,mazo


          
