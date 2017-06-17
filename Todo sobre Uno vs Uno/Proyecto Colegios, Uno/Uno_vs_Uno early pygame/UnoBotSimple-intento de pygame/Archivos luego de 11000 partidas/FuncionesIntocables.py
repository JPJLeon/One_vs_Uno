#Creado por:    Juan Pablo Leon 
#               Yeison Fernandez
#               Jordan Esquivel

from FuncionReparto import *
import pygame, sys, time
from pygame.locals import *
from Utilidades import *

pygame.init()
screen = pygame.display.set_mode(DIMENSION)
pygame.display.set_caption("One Vs Uno")
fondo_juego = pygame.image.load("img/"+"fondo.jpg").convert()
pensando = pygame.image.load("img/"+"pensando.jpg").convert()

def dibujar(mano_jugador,mano_bot,imagenes_cartas,screen,cem,fondo_juego):
    x=4
    y=414
    screen.blit(fondo_juego, (0, 0))
    contador=0
    for cartas in mano_jugador:
        contador=contador+1
        if contador == 16:
            y=y+110
            x=4
        screen.blit(imagenes_cartas[cartas],(x,y))
        x=x+56
        
    contador=0
    x=4
    y=20
    for cartas in mano_bot:
        contador=contador+1
        if contador == 15:
            y=y+110
            X=4
        screen.blit(imagenes_cartas[("N","CUBIERTA")],(x,y))
        x=x+56
    
    x=397
    y=262
    screen.blit(imagenes_cartas[cem[-1]],(x,y))
    screen.blit(imagenes_cartas[("N","MAZO")],(700,237))
    screen.blit(imagenes_cartas[("N","PASO")],(10,262))
    pygame.display.flip()

def checkear_jugada_list(carta):
    archivo=open(str(carta)+'.txt')
    lista=[]
    for linea in archivo:
        linea=linea.split(" ")
        for elemento in linea:
            elemento=elemento.split(';')
            lista.append(elemento)
    archivo.close()            
    return lista

def comprobar_jug(carta,cementerio): #Comprobar que carta se jugo, si es legal 
    color,tipo=carta             #y si tiene algun efecto en la partida
    color_c,tipo_c=cementerio[-1]
    if color == color_c or tipo == tipo_c or color == "N":
        return (True,tipo)
    else:
        return (False,1)


def combinaciones(colores,numeros,especiales):
    comb=list()
    for i in colores:
        for k in numeros:
            comb.append((i,k))
    return comb+especiales


def revolver_el_mazo(mazo,cementerio):          
    for i in range(len(cementerio)-1):      
        if cementerio[0][1]=="+4" or cementerio[0][1]=="CC":
            mazo.append(("N",cem[0][1]))
        else:                           #Funcion que revuelve el mazo con
            mazo.append(cem[0])     #el cementerio cuando se acabaron
        cementerio.remove(cem[0])       #las cartas del mazo, transformando     
                                                #todos las cartas +4 devuelta al color
    return mazo,cementerio                  #negro "N" para su nuevo uso

def checkear_jugada_dicc(carta):
    archivo=open(str(carta)+'.txt')
    diccionario={}
    for linea in archivo:
        linea=linea.split(" ")
        for elemento in linea:
            elemento=elemento.split(';')
            diccionario[tuple((elemento[0],elemento[1]))]=elemento[2]
    return diccionario

############################################################### Inicio ##########################################################################
######################################################## Funcion Contra_Ataque ##################################################################

def contra_ataque(carta_trampa_jugada,turno,manobot,manojugador,cementerio,mazo,imagenes_cartas,screen,fondo_juego):
          
    #print "---------Iniciando ciclo de trampa-------------"
    color,numero=carta_trampa_jugada
    numero_a_robar=int(numero)
    booleano=0
    while booleano==0:
############################################ Jugador  ##########################################################
        if turno%2==0:
            dibujar(manojugador,manobot,imagenes_cartas,screen,cementerio,fondo_juego)
                        
            print "UnoBot ha lanzado una carta trampa: ",carta_trampa_jugada
            while True:
                print ""
                print "Cartas en mano: ",manojugador
                print ""
                jugada_contra_ataque=raw_input("Desea lanzar una carta trampa como respuesta?(Si=S; No=N): ")
                                
                if jugada_contra_ataque=="S":
                    print ""
                                        
                    color_contra_ataque=raw_input("Ingrese el color de su carta: ")
                    tipo_contra_ataque=(raw_input("Ingrese el tipo de su carta: "))
                    carta_contra_ataque=tuple((color_contra_ataque,tipo_contra_ataque))
                                        
                    if tipo_contra_ataque>=numero and carta_contra_ataque in manojugador and (tipo_contra_ataque=="+2" or tipo_contra_ataque=="+4"):
                        manojugador.remove(carta_contra_ataque)
                                                
                        if tipo_contra_ataque=="+4":
                            color_contra_ataque=raw_input("Que color eliges? (Y= AMARILLO, B= AZUL,R= ROJO,G= VERDE): ")
                                                        
                        carta_contra_ataque=tuple((color_contra_ataque,tipo_contra_ataque))
                                                
                        cementerio.append(carta_contra_ataque)
                                                
                        dibujar(manojugador,manobot,imagenes_cartas,screen,cementerio,fondo_juego)
                                                
                        numero=tipo_contra_ataque
                        numero_a_robar+=int(tipo_contra_ataque)
                        carta_trampa_jugada=carta_contra_ataque
                        turno+=1
                                                
                        break
                                        
                    else:
                        print "Jugada invalida, aplicando penalizacion."
                        for i in range(numero_a_robar+2):
                            if len(mazo)==0:
                                mazo,cementerio=revolver_el_mazo(mazo,cementerio)
                            manojugador,mazo=carta_aleatoria(manojugador,mazo)
                                                        
                            booleano=1
                            break
                                                
                elif jugada_contra_ataque=="N":
                    for i in range(numero_a_robar):
                        if len(mazo)==0:
                            mazo,cementerio=revolver_el_mazo(mazo,cementerio)
                        manojugador,mazo=carta_aleatoria(manojugador,mazo)
                                                
                    booleano=1
                    break
                                        
############################################ UnoBot ############################################################
        elif turno%2==1:
            dibujar(manojugador,manobot,imagenes_cartas,screen,cementerio,fondo_juego)
            screen.blit(pensando,(350,20))
            pygame.display.flip()
            time.sleep(5)
            while True:                
                mejor_carta=0
                mejor_puntuacion=0
                                        
                opciones=checkear_jugada_dicc(str(carta_trampa_jugada)+'T')
                for color_mano,tipo_mano in manobot:
                    if (color_mano,tipo_mano)in opciones:
                        if int(opciones[(color_mano,tipo_mano)])>=mejor_puntuacion:
                            mejor_carta=(color_mano,tipo_mano)
                            mejor_puntuacion=int(opciones[(color_mano,tipo_mano)])
                if mejor_carta==0:
                    for i in range(numero_a_robar):
                        if len(mazo)==0:
                            mazo,cementerio=revolver_el_mazo(mazo,cementerio)
                        if len(manobot)<30:
                            manobot,mazo=carta_aleatoria(manobot,mazo)
                                                       
                    booleano=1                                     
                    break
                else:
                    jugada_contra_ataque=mejor_carta
                    if jugada_contra_ataque[1]==carta_trampa_jugada[1] or jugada_contra_ataque[1]=='+4':
                        manobot.remove(jugada_contra_ataque)
                                                
                        if jugada_contra_ataque[0]=='N':
                            Y=0
                            G=0
                            B=0
                            R=0
                            for cc,_ in manobot:
                                if cc=='Y':
                                    Y+=1
                                if cc=='B':
                                    B+=1
                                if cc=='G':
                                    G+=1
                                if cc=='R':
                                    R+=1
                            Dicc={}
                            Dicc[Y]='Y'
                            Dicc[G]='G'
                            Dicc[B]='B'
                            Dicc[R]='R'
                            color_contra_ataque=Dicc[max(Y,G,B,R)]
                            cementerio.append((color_contra_ataque,jugada_contra_ataque[1]))
                            carta_trampa_jugada=(color_contra_ataque,jugada_contra_ataque[1])
                        if jugada_contra_ataque[0]!='N':
                            cementerio.append(jugada_contra_ataque)
                            carta_trampa_jugada=jugada_contra_ataque
                                                        
                        dibujar(manojugador,manobot,imagenes_cartas,screen,cementerio,fondo_juego)
                                                
                        numero=jugada_contra_ataque[1]
                        numero_a_robar+=int(jugada_contra_ataque[1])
                        turno+=1
                        break
                    else:
                        print "------------UnoBotDos se ha equivocado----------"
                        print "jugada de UnoBotDos: ",jugada_contra_ataque, "carta en cementerio:",cementerio[-1]
                                                
                        for i in range(numero_a_robar+2):
                            if len(mazo)<=1:
                                mazo,cementerio=revolver_el_mazo(mazo,cementerio)
                            if len(manobot)<30:
                                manobot,mazo=carta_aleatoria(manobot,mazo)
                                                                
                            booleano=1                                     
                            break
    return turno,manobot,manojugador,cementerio,mazo

########################################################################## Fin #########################################################################
################################################################## Funcion Contra_Ataque ################################################################


def comprobar_efecto(efecto,manobot,manojugador,turno,jugada,cementerio,mazo,imagenes_cartas,screen,fondo_juego): 
                                                        #Comprueba el efecto de la carta lanzada
    if efecto == "SKIP" or efecto == "REV":         #y realiza distintas acciones dependiendo
        cementerio.append(jugada)               #del tipo de la carta
        turno +=1
                
        return turno,manobot,manojugador,cementerio,mazo
        
    if efecto == "+2":
        cementerio.append(jugada)
        turno +=1
                
        turno,manobot,manojugador,cementerio,mazo=contra_ataque(jugada,turno,manobot,manojugador,cementerio,mazo,imagenes_cartas,screen,fondo_juego)
                
        return turno,manobot,manojugador,cementerio,mazo
        
    if efecto == "+4":
        if turno%2==1:
            Y=0
            G=0
            B=0
            R=0
            for cc,_ in manobot:
                if cc=='Y':
                    Y+=1
                if cc=='B':
                    B+=1
                if cc=='G':
                    G+=1
                if cc=='R':
                    R+=1
                                
                        
            Dicc={}
            Dicc[Y]='Y'
            Dicc[G]='G'
            Dicc[B]='B'
            Dicc[R]='R'
            color_elegido=Dicc[max(Y,G,B,R)]
            jugada=tuple((color_elegido,jugada[1]))
            cementerio.append(jugada)
            turno +=1
                        
            turno,manobot,manojugador,cementerio,mazo=contra_ataque(jugada,turno,manobot,manojugador,cementerio,mazo,imagenes_cartas,screen,fondo_juego)
                        
            return turno,manobot,manojugador,cementerio,mazo
                              
        else:
            screen.blit(imagenes_cartas[("Y","+4")],(150,265))
            screen.blit(imagenes_cartas[("B","+4")],(210,265))
            screen.blit(imagenes_cartas[("R","+4")],(270,265))
            screen.blit(imagenes_cartas[("G","+4")],(330,265))
            pygame.display.flip()
            
            pregunta = raw_input("Que color eliges? (Y= AMARILLO, B= AZUL,R= ROJO,G= VERDE): ")
            jugada=tuple((pregunta,jugada[1]))
            cementerio.append(jugada)
            turno +=1
                        
            turno,manobot,manojugador,cementerio,mazo=contra_ataque(jugada,turno,manobot,manojugador,cementerio,mazo,imagenes_cartas,screen,fondo_juego)
                        
            return turno,manobot,manojugador,cementerio,mazo
                       
                    
    if efecto == "CC":
                
        if turno%2==1:
            Y=0
            G=0
            B=0
            R=0
            for cc,_ in manobot:
                if cc=='Y':
                    Y+=1
                if cc=='B':
                    B+=1
                if cc=='G':
                    G+=1
                if cc=='R':
                    R+=1
            Dicc={}
            Dicc[Y]='Y'
            Dicc[G]='G'
            Dicc[B]='B'
            Dicc[R]='R'
            color_elegido=Dicc[max(Y,G,B,R)]
            jugada=tuple((color_elegido,jugada[1]))
            cementerio.append(jugada)
                        
            return turno,manobot,manojugador,cementerio,mazo
        else:
            screen.blit(imagenes_cartas[("Y","CC")],(150,265))
            screen.blit(imagenes_cartas[("B","CC")],(210,265))
            screen.blit(imagenes_cartas[("R","CC")],(270,265))
            screen.blit(imagenes_cartas[("G","CC")],(330,265))
            pygame.display.flip()
            
            pregunta = raw_input("Que color eliges? (Y= AMARILLO, B= AZUL,R= ROJO,G= VERDE): ")
            jugada= (pregunta,jugada[1])
            cementerio.append(jugada)
            return turno,manobot,manojugador,cementerio,mazo
        
    cementerio.append(jugada)
    return turno,manobot,manojugador,cementerio,mazo
