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

fondo_juego = pygame.image.load("img1/"+"fondo.jpg").convert()
if fondo_juego.get_size() != DIMENSION: 
    fondo_juego = pygame.transform.scale(fondo_juego, DIMENSION)

def dibujar(mano_jugador,mano_bot,imagenes_cartas,screen,cem):
    screen.blit(fondo_juego,(0,0))
    x=4
    y=414
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
            x=4
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

def contra_ataque(carta_trampa_jugada,turno,manobot,manojugador,cementerio,mazo,imagenes_cartas,screen):
          
    #print "---------Iniciando ciclo de trampa-------------"
    color,numero=carta_trampa_jugada
    numero_a_robar=int(numero)
    booleano=0
    dibujar(manojugador,manobot,imagenes_cartas,screen,cementerio)
    screen.blit(imagenes_cartas[("N","CICLOTRAMPA")],(540,237))
    pygame.display.flip()
    
    while booleano==0:
############################################ Jugador  ##########################################################
        if turno%2==0:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    corriendo = False
                if evento.type == KEYDOWN and evento.key == K_ESCAPE:
                    corriendo = False
                    
                if evento.type == MOUSEBUTTONDOWN:
                    
                    p_m=pygame.mouse.get_pos() #p_m = posicion_mouse
                    print p_m[0],p_m[1]
                    
                    if p_m[0]>=10 and p_m[0]<=110 and p_m[1]>=262 and p_m[1]<=362:
                        
                        pygame.display.flip()
                        for i in range(numero_a_robar):
                            if len(mazo)==0:
                                mazo,cementerio=revolver_el_mazo(mazo,cementerio)
                            manojugador,mazo=carta_aleatoria(manojugador,mazo)                               
                        booleano=1
                        break
                    
                    else:
                        xmin=4; xmax=58     #coordenadas que ocupa cada carta
                        ymin=414; ymax=514
                        
                        for carta in manojugador:
                            
                            if xmax>850:
                                xmin=4; xmax=58
                                ymin=524; ymax=624
                                
                            if p_m[0]>=xmin and p_m[0]<=xmax and p_m[1]>=ymin and p_m[1]<=ymax:
                                
                                print p_m[0]>xmin,p_m[0]<xmax
        
                                if carta[1]>=numero and (carta[1]=="+2" or carta[1]=="+4"):
                                    manojugador.remove(carta)
                                    dibujar(manojugador,manobot,imagenes_cartas,screen,cementerio)
                                    jugada=carta
                                    numero_a_robar+=int(carta[1])
                                    
                                    if carta[1]=="+4":
                                        screen.blit(imagenes_cartas[("Y","+4")],(150,265))
                                        screen.blit(imagenes_cartas[("B","+4")],(210,265))
                                        screen.blit(imagenes_cartas[("R","+4")],(270,265))
                                        screen.blit(imagenes_cartas[("G","+4")],(330,265))
                                        pygame.display.flip()

                                        ciclo=True
                                        while ciclo:
                                            for evento in pygame.event.get():
                                                if evento.type == pygame.QUIT:
                                                    corriendo = False
                                                if evento.type == KEYDOWN and evento.key == K_ESCAPE:
                                                    corriendo = False
                                                if evento.type == MOUSEBUTTONDOWN:
                                                    p_m=pygame.mouse.get_pos()
                                                    if p_m[1]>=265 and p_m[1]<=365:
                                                        if p_m[0]>=150 and p_m[0]<=204:
                                                            jugada=tuple(("Y","+4"))
                                                            ciclo=False
                                                            break
                                                        elif p_m[0]>=210 and p_m[0]<=264:
                                                            jugada=tuple(("B","+4"))
                                                            ciclo=False
                                                            break
                                                        elif p_m[0]>=270 and p_m[0]<=324:
                                                            jugada=tuple(("R","+4"))
                                                            ciclo=False
                                                            break
                                                        elif p_m[0]>=330 and p_m[0]<=384:
                                                            jugada=tuple(("G","+4"))
                                                            ciclo=False
                                                            break
            
                                    cementerio.append(jugada)
                                    dibujar(manojugador,manobot,imagenes_cartas,screen,cementerio)
                                    
                                    
                                    if len(manojugador)==0:
                                        anotherone=1
                                        pygame.display.flip()
                                        break
                                    else:
                                        turno+=1
                                        pygame.display.flip()
                                        break
                                else:
                                    for i in range(numero_a_robar+2):
                                        if len(mazo)==0:
                                            mazo,cementerio=revolver_el_mazo(mazo,cementerio)
                                        manojugador,mazo=carta_aleatoria(manojugador,mazo)
                                                        
                                    booleano=1
                                    break
                            xmin+=56;xmax+=56
                                        
############################################ UnoBot ############################################################
        elif turno%2==1:
            dibujar(manojugador,manobot,imagenes_cartas,screen,cementerio)
            screen.blit(imagenes_cartas[("N","PENSANDO")],(350,20))
            screen.blit(imagenes_cartas[("N","CICLOTRAMPA")],(540,237))
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
                
                if mejor_carta==0:  #One no tiene alguna posible jugada, por lo que roba la cantidad
                    for i in range(numero_a_robar): #de cartas establecida por las trampas
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
                                                        
                        dibujar(manojugador,manobot,imagenes_cartas,screen,cementerio)
                        screen.blit(imagenes_cartas[("N","CICLOTRAMPA")],(540,237))
                        pygame.display.flip()
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


def comprobar_efecto(efecto,manobot,manojugador,turno,jugada,cementerio,mazo,imagenes_cartas,screen): 
                                                        #Comprueba el efecto de la carta lanzada
    if efecto == "SKIP" or efecto == "REV":         #y realiza distintas acciones dependiendo
        cementerio.append(jugada)               #del tipo de la carta
        turno +=1
        dibujar(manojugador,manobot,imagenes_cartas,screen,cementerio)        
        return turno,manobot,manojugador,cementerio,mazo
        
    if efecto == "+2":
        cementerio.append(jugada)
        turno +=1
        dibujar(manojugador,manobot,imagenes_cartas,screen,cementerio)        
        turno,manobot,manojugador,cementerio,mazo=contra_ataque(jugada,turno,manobot,manojugador,cementerio,mazo,imagenes_cartas,screen)
                
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
            dibujar(manojugador,manobot,imagenes_cartas,screen,cementerio)
            turno +=1
                        
            turno,manobot,manojugador,cementerio,mazo=contra_ataque(jugada,turno,manobot,manojugador,cementerio,mazo,imagenes_cartas,screen)
                        
            return turno,manobot,manojugador,cementerio,mazo
                              
        else:
            screen.blit(imagenes_cartas[("Y","+4")],(150,265))
            screen.blit(imagenes_cartas[("B","+4")],(210,265))
            screen.blit(imagenes_cartas[("R","+4")],(270,265))
            screen.blit(imagenes_cartas[("G","+4")],(330,265))
            pygame.display.flip()

            siclo=True
            while siclo:
                for evento in pygame.event.get():
                    if evento.type == pygame.QUIT:
                        corriendo = False
                    if evento.type == KEYDOWN and evento.key == K_ESCAPE:
                        corriendo = False
                    if evento.type == MOUSEBUTTONDOWN:
                        p_m=pygame.mouse.get_pos()
                        if p_m[1]>=265 and p_m[1]<=365:
                            if p_m[0]>=150 and p_m[0]<=204:
                                jugada=tuple(("Y","+4"))
                                siclo=False
                                break
                            elif p_m[0]>=210 and p_m[0]<=264:
                                jugada=tuple(("B","+4"))
                                siclo=False
                                break
                            elif p_m[0]>=270 and p_m[0]<=324:
                                jugada=tuple(("R","+4"))
                                siclo=False
                                break
                            elif p_m[0]>=330 and p_m[0]<=384:
                                jugada=tuple(("G","+4"))
                                siclo=False
                                break
            
            cementerio.append(jugada)
            dibujar(manojugador,manobot,imagenes_cartas,screen,cementerio)
            turno +=1
            turno,manobot,manojugador,cementerio,mazo=contra_ataque(jugada,turno,manobot,manojugador,cementerio,mazo,imagenes_cartas,screen)
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
            dibujar(manojugador,manobot,imagenes_cartas,screen,cementerio)            
            return turno,manobot,manojugador,cementerio,mazo
        else:
            screen.blit(imagenes_cartas[("Y","CC")],(150,265))
            screen.blit(imagenes_cartas[("B","CC")],(210,265))
            screen.blit(imagenes_cartas[("R","CC")],(270,265))
            screen.blit(imagenes_cartas[("G","CC")],(330,265))
            pygame.display.flip()
            siclo=True
            while siclo:
                for evento in pygame.event.get():
                    if evento.type == pygame.QUIT:
                        corriendo = False
                    if evento.type == KEYDOWN and evento.key == K_ESCAPE:
                        corriendo = False
                    if evento.type == MOUSEBUTTONDOWN:
                        p_m=pygame.mouse.get_pos()
                        if p_m[1]>=265 and p_m[1]<=365:
                            if p_m[0]>=150 and p_m[0]<=204:
                                jugada=tuple(("Y","CC"))
                                siclo=False
                                break
                            elif p_m[0]>=210 and p_m[0]<=264:
                                jugada=tuple(("B","CC"))
                                siclo=False
                                break
                            elif p_m[0]>=270 and p_m[0]<=324:
                                jugada=tuple(("R","CC"))
                                siclo=False
                                break
                            elif p_m[0]>=330 and p_m[0]<=384:
                                jugada=tuple(("G","CC"))
                                siclo=False
                                break
            
            cementerio.append(jugada)
            dibujar(manojugador,manobot,imagenes_cartas,screen,cementerio)
            return turno,manobot,manojugador,cementerio,mazo
        
    cementerio.append(jugada)
    return turno,manobot,manojugador,cementerio,mazo
