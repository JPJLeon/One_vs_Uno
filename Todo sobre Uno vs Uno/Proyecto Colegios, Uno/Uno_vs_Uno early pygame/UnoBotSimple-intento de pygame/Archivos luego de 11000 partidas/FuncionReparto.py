#Creado por:    Juan Pablo Leon 
#               Yeison Fernandez
#               Jordan Esquivel

from FuncionCartaAleatoria import *

def reparto(mazo,cementerio):   #Funcion que se utiliza al inicio de
        manojugador=[]          #cada partida. Se generan las manos
        manobot=[]              #de cartas del jugador y del Unobot
        for i in range(2):      #sacando cartas al azar del mazo
                if i==0:
                        for k in range(16):
                                #Se llena la mano del jugador
                                #del jugador con 8 cartas
                                carta_aleatoria(manojugador,mazo)             
                                
                if i==1:
                        for l in range(8):
                                #Se llena la mano del UnoBot
                                #con 8 cartas
                                carta_aleatoria(manobot,mazo)
                                
        while True:
                c,n=choice(mazo)                                       
                if n in ['0','1','2','3','4','5','6','7','8','9']:
                        car=(c,n)               #se elige una carta al "azar" del                    
                        mazo.remove(car)        #mazo para que sea la primera carta 
                        break                   #del cementerio, asegurando que no sea 
        cementerio.append(car)                  #una carta trampa.
        return mazo,cementerio,manojugador,manobot
