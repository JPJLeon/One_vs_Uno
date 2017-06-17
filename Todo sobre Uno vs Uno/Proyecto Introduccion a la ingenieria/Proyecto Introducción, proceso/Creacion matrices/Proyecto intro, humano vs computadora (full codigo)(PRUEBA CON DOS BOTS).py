from random import *
from Funciones Basicas import *
from Funcion Contraataque import *
from Funcion Comprobar Efecto import *

juegos=0
while juegos<250000:
        juegos+=1
        num=('0','1','2','3','4','5','6','7','8','9',"+2","REV","SKIP")
        colors=("Y","B","G","R")
        specials=[("N","+4"),("N","+4"),("N","+4"),("N","+4"),("N","CC"),("N","CC"),("N","CC"),("N","CC")]
        mazo=combinaciones(colors,num,specials)
        l1=[]
        l2=[]
        lista_trampa1=[]
        lista_trampa2=[]
        contador_rob_1=0
        contador_rob_bot=0
        contador_tir_1=0
        contador_tir_bot=0
        cem=[]
        turno=0
        mazoor,juga1,juga2=reparto(mazo)
        anotherone=0
        while True:
                if anotherone==1:
                        break
                        
                    
################################################# Turno Computadora 1 ########################################################################
                if turno%2==0:
                        while True:
                                #print "---------Inicio turno UnoBotUno-------------"
                                color_actual,tipo_actual=cem[-1]
                                if len(mazoor)==0:
                                        revolver_el_mazo()
                                        
                                cartas_en_mano=juga1
                                
                                jugada1="R"
                                for color_mano,tipo_mano in cartas_en_mano:
                                       if color_mano==color_actual or tipo_mano==tipo_actual or color_mano=="N":
                                               jugada1="B"
                                
                                        
                                if jugada1=="R":
                                        #print "UnoBot ha robado carta"
                                        carta_aleatoria(juga1)
                                        contador_rob_1+=1
                                        jugada1="P"
                                        for color_mano,tipo_mano in cartas_en_mano:
                                               if color_mano==color_actual or tipo_mano==tipo_actual or color_mano=="N":
                                                       jugada1="B"
                                       
                                        
                                        if jugada1=="P":
                                                turno+=1
                                                #print "---------UnoBotUno ha pasado el turno-------------"
                                               
                                                break
                                        
                                if jugada1=="B":
                                        mejor_puntuacion=0
                                        mejor_carta=0
                                        diccionario_de_opciones=checkear_jugada_dicc(cem[-1])
                                        
                                        for color_mano,tipo_mano in cartas_en_mano:
                                                if (color_mano,tipo_mano)in diccionario_de_opciones:
                                                        if diccionario_de_opciones[(color_mano,tipo_mano)]>=mejor_puntuacion:
                                                                
                                                                
                                                                mejor_carta=(color_mano,tipo_mano)
                                                                mejor_puntuacion=diccionario_de_opciones[(color_mano,tipo_mano)]
                                        #print mejor_carta
                                        jugadia=comprobar_jug(mejor_carta)
                                        
                                        if jugadia[0]==True:
                                                juga1.remove(mejor_carta)
                                                contador_tir_1+=1
                                                
                                                if mejor_carta[1]=='+4' or mejor_carta[1]=='CC':
                                                        l1.append((cem[-1],('N',mejor_carta[1])))
                                                if mejor_carta[1]!='+4' and mejor_carta[1]!='CC':
                                                        l1.append((cem[-1],mejor_carta[1]))
                                                        
                                                if len(juga1)==0:
                                                        anotherone=1
                                                        #print "---------UnoBotUno ha ganado la partida-------------"
                                                        #print "\n\n\n"
                                                        break
                                                turno,contador_rob_bot,contador_tir_bot,contador_rob_1,contador_tir_1=comprobar_efecto(jugadia[1],juga1,turno,mejor_carta,contador_rob_bot,contador_tir_bot,contador_rob_1,contador_tir_1)
                                                
                                                #print "UnoBot ha jugado la carta",mejor_carta
                                                
                                                if len(juga1)!=0:
                                                        turno+=1
                                                        #print "---------Fin turno UnoBotUno-------------"
                                                        #print "\n\n\n"
                                                        break
                                        elif jugadia[0]==False:
                                                carta_aleatoria(juga1)
                                                carta_aleatoria(juga1)
                                                turno+=1
                                                #print "---------Fin turno UnoBotUno-------------"
                                                #print "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                                                break
                        
                                                
################################################# Turno Computadora 2 ########################################################################
                elif turno%2==1:
                        
                        while True:
                                #print "---------Inicio turno UnoBotDos-------------"
                                color_actual,tipo_actual=cem[-1]
                                if len(mazoor)==0:
                                        revolver_el_mazo()
                                        
                                cartas_en_mano=juga2
                                mejor_puntuacion=0
                                mejor_carta=0
                                #opciones=checkear_jugada_dicc(cem[-1])
                                #for color_mano,tipo_mano in cartas_en_mano:
                                #                if (color_mano,tipo_mano)in opciones:
                                #                        if int(opciones[(color_mano,tipo_mano)])>=mejor_puntuacion:
                                #                                
                                #                                
                                #                                mejor_carta=(color_mano,tipo_mano)
                                #                                mejor_puntuacion=int(diccionario_de_opciones[(color_mano,tipo_mano)])
                                #if mejor_carta==0:
                                #       carta_aleatoria(juga2)
                                #       contador_rob_bot+=1
                                #
                                #for color_mano,tipo_mano in cartas_en_mano:
                                #                if (color_mano,tipo_mano)in opciones:
                                #                        if int(opciones[(color_mano,tipo_mano)])>=mejor_puntuacion:
                                #                                
                                #                                
                                #                                mejor_carta=(color_mano,tipo_mano)
                                #                                mejor_puntuacion=int(diccionario_de_opciones[(color_mano,tipo_mano)])
                                #if mejor_carta==0:
                                #       turno+=1
                                #       break
                                #else:
                                #       jugadia=comprobar_jug(mejor_carta)
                                #       if jugadia[0]==True:
                                #               juga2.remove(mejor_carta)
                                #               contador_tir_bot+=1
                                #               l2.append((cem[-1],mejor_carta))
                                #               if len(juga2)==0:
                                #                       anotherone=1
                                #                       print "---------UnoBotDos ha ganado la partida-------------"
                                #                       break
                                #               turno,contador_rob_bot,contador_tir_bot,contador_rob_1,contador_tir_1=comprobar_efecto(jugadia[1],juga1,turno,mejor_carta,contador_rob_bot,contador_tir_bot,contador_rob_1,contador_tir_1)
                                #               if len(juga2)!=0:
                                #                       turno+=1
                                #                       break
                                #       elif jugadia[0]==False:
                                #               print "------- UnoBotDos se ha equivocado -------"
                                #               contador_rob_bot+=2
                                #               l2.append((cem[-1],mejor_carta))
                                #               carta_aleatoria(juga2)
                                #               carta_aleatoria(juga2)
                                #               turno+=1
                                #               break
                                
                                
                #print "\n\n\n\n\n"
        puntosb=obtener_puntuacion_bot(l2,juga2,contador_tir_1,contador_tir_bot,contador_rob_1,contador_rob_bot,lista_trampa_2)
        puntosj=obtener_puntuacion_jug(l1,juga1,contador_tir_1,contador_tir_bot,contador_rob_1,contador_rob_bot,lista_trampa_1) 
        if juegos%1000==0:
        
                print "\n Puntuacion UnoBotDos:",puntosb
                print "\n Puntuacion UnoBotUno:",puntosj
                print "---------------ARCHIVOS MODIFICADOS--------"
                print juegos
        modificar_archivos(l1,puntosj)
        modificar_archivos(l2,puntosb)
        













                                                       

