#Creado por:    Juan Pablo Leon 
#               Yeison Fernandez
#               Jordan Esquivel

from FuncionesIntocables import *
#### Modulos de Pygame #########

juegos=0
#############################

if fondo_juego.get_size() != DIMENSION: 
    fondo_juego = pygame.transform.scale(fondo_juego, DIMENSION)
if pensando.get_size() != (100,54):
        pensando = pygame.transform.scale(pensando, (150,81))
###################################
    
imagenes_cartas = dict()

for tuplacarta, archivo in IMAGENES_CARTAS.items():
    imagen = pygame.image.load("img/"+archivo).convert_alpha()

    if imagen.get_size() != (54, 100):
        imagen = pygame.transform.scale(imagen, (54, 100))
    if tuplacarta[1]=="MAZO":
        imagen = pygame.transform.scale(imagen, (81, 150))
    if tuplacarta[1]=="PASO":
        imagen = pygame.transform.scale(imagen, (100, 100))    
    imagenes_cartas[tuplacarta] = imagen
####################################
    
screen.blit(fondo_juego, (0, 0))
pygame.display.flip()
ENDGAME=False
#################################

#################################    
while ENDGAME==False:
    juegos+=1
    numeros=('0','1','2','3','4','5','6','7','8','9',"+2","REV","SKIP",'0','1','2','3','4','5','6','7','8','9',"+2","REV","SKIP")
    colores=("Y","B","G","R")
    especiales=[("N","+4"),("N","+4"),("N","+4"),("N","+4"),("N","CC"),("N","CC"),("N","CC"),("N","CC")]
    mazo_combinaciones=combinaciones(colores,numeros,especiales)
    cem=[]
    turno=0
    mazo,cem,mano_jugador,mano_bot=reparto(mazo_combinaciones,cem)
                
    anotherone=0
    while True:
        if anotherone==1:
            break

################################################# Turno Jugador ########################################################################
        if turno%2==0:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    ENDGAME=True
                                
            screen.blit(fondo_juego, (0, 0))
            pygame.display.flip()
            while True:
                                    
                print "---------Inicio turno Jugador-------------"
                print ""
                                        
                dibujar(mano_jugador,mano_bot,imagenes_cartas,screen,cem,fondo_juego)
                                        
                print("La carta actual es: "),cem[-1]
                print ""
                print "A UnoBot le quedan",len(mano_bot),"cartas en la mano"
                print ""
                if len(mazo)==0:
                    mazo,cem=revolver_el_mazo(mazo,cem)
                                                
                print("Tus cartas son: "),mano_jugador
                print ""
                jugada1=0
                while jugada1!="R" and jugada1!="B":
                    jugada1=raw_input("Que desea hacer?(R=ROBAR,B=BOTAR): ")
                                                
                if jugada1=="R":
                    mano_jugador,mazo=carta_aleatoria(mano_jugador,mazo)
                    print "Ha robado la carta: ",mano_jugador[-1]
                    print ""
                                                
                    dibujar(mano_jugador,mano_bot,imagenes_cartas,screen,cem,fondo_juego)
                                                
                    print("Tus cartas son: "),mano_jugador
                    print ""
                    jugada1=raw_input("Que desea hacer?(P=PASAR,B=BOTAR): ")
                    if jugada1=="P":
                        turno+=1
                        print "---------Fin turno Jugador-------------"
                        print ""
                        pygame.display.flip()
                        break
                                                
                if jugada1=="B":
                    color111=0
                    tipo111=0
                    while color111 not in ("B","Y","R","G","N") or tipo111 not in ("+2","+4","REV","CC","SKIP","0","1","2","3","4","5","6","7","8","9",):
                        color111=raw_input("Ingrese el color de su carta: ")
                        tipo111=(raw_input("Ingrese el tipo de su carta: "))
                        
                    jugada111=tuple((color111,tipo111))
                    jugada_legalizada=comprobar_jug(jugada111,cem)
                                                
                    if jugada_legalizada[0]==True:
                        dibujar(mano_jugador,mano_bot,imagenes_cartas,screen,cem,fondo_juego)
                        mano_jugador.remove(jugada111)
                        turno,mano_bot,mano_jugador,cem,mazo=comprobar_efecto(jugada_legalizada[1],mano_bot,mano_jugador,turno,jugada111,cem,mazo,imagenes_cartas,screen,fondo_juego)
                                                        
                        if len(mano_jugador)==0:
                            anotherone=1
                            print "---------Jugador ha ganado la partida-------------"
                            print ""
                            pygame.display.flip()
                            break
                        else:
                            turno+=1
                            print "---------Fin turno Jugador-------------"
                            print ""
                            pygame.display.flip()
                            break
                    elif jugada_legalizada[0]==False:
                        if len(mazo)<2:
                            mazo,cem=revolver_el_mazo(mazo,cem)
                                                                
                        mano_jugador,mazo=carta_aleatoria(mano_jugador,mazo)
                        mano_jugador,mazo=carta_aleatoria(mano_jugador,mazo)
                        turno+=1
                                                        
                        pygame.display.flip()
                        print "---------JUGADA ILEGAL-------------"
                        print "---------Fin turno Jugador -------------"
                        print ""
                        break
                      
################################################# Turno UnoBot ########################################################################
        elif turno%2==1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    ENDGAME=True
                pygame.display.flip()      
            while True:
                print "---------Inicio turno UnoBot-------------"
                dibujar(mano_jugador,mano_bot,imagenes_cartas,screen,cem,fondo_juego)
                screen.blit(pensando,(350,20))
                    
                print "Pensando............"
                pygame.display.flip()
                time=pygame.time.delay(5000)
                            
                if time!=0:
                    color_actual,tipo_actual=cem[-1]
                    if len(mazo)==0:
                        mazo,cem=revolver_el_mazo(mazo,cem)
                        
                    mejor_puntuacion=0
                    mejor_carta=0
                    opciones=checkear_jugada_dicc(cem[-1])
    
                    for color_mano,tipo_mano in mano_bot:
                        if (color_mano,tipo_mano)in opciones:
                            if int(opciones[(color_mano,tipo_mano)])>=mejor_puntuacion:                  
                                mejor_carta=(color_mano,tipo_mano)
                                mejor_puntuacion=int(opciones[(color_mano,tipo_mano)])
                    
                    if mejor_carta==0:
                        if len(mano_bot)<30:
                            mano_bot,mazo=carta_aleatoria(mano_bot,mazo)
                        print "UnoBot ha robado una carta"
                        
                    mejor_puntuacion=0
                    mejor_carta=0
                    for color_mano,tipo_mano in mano_bot:
                        if (color_mano,tipo_mano)in opciones:
                            if int(opciones[(color_mano,tipo_mano)])>=mejor_puntuacion:
                                mejor_carta=(color_mano,tipo_mano)
                                mejor_puntuacion=int(opciones[(color_mano,tipo_mano)])
                    
                    if mejor_carta==0:
                        print "--------- UnoBot ha pasado el turno-------\n"
                        turno+=1
                        break
                    else:
                        jugada_legalizada=comprobar_jug(mejor_carta,cem)
                        
                        if jugada_legalizada[0]==True:
                            print "UnoBot ha lanzado la carta:",mejor_carta
                            mano_bot.remove(mejor_carta)
                                                            
                            dibujar(mano_jugador,mano_bot,imagenes_cartas,screen,cem,fondo_juego)
                                                            
                            if len(mano_bot)==0:
                                anotherone=1
                                print "---------UnoBot ha ganado la partida-------------\n"
                                break
                            
                            turno,mano_bot,mano_jugador,cem,mazo=comprobar_efecto(jugada_legalizada[1],mano_bot,mano_jugador,turno,mejor_carta,cem,mazo,imagenes_cartas,screen,fondo_juego)
                            
                            if len(mano_bot)!=0:
                                turno+=1
                                print "---------Fin turno UnoBot---------\n"
                                break
                             
                        elif jugada_legalizada[0]==False:
                            
                            print "------- UnoBot se ha equivocado -------\n"
                            print "Carta en el cementerio:",cem[-1],", carta que trato de jugar UnoBot:",mejor_carta
                            
                            if len(mazo)<2:
                                mazo,cem=revolver_el_mazo(mazo,cem)
                                
                            if len(mano_bot)<30:
                                mano_bot,mazo=carta_aleatoria(mano_bot,mazo)
                                mano_bot,mazo=carta_aleatoria(mano_bot,mazo)
                            turno+=1
                            break
                        
   
    print "---------------ARCHIVOS MODIFICADOS--------"





pygame.quit()
sys.exit()
