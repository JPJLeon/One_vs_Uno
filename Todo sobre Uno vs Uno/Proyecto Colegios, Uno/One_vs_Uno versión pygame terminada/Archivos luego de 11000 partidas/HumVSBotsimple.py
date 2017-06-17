#Creado por:    Juan Pablo Leon 
#               Yeison Fernandez
#               Jordan Esquivel

from FuncionesIntocables import *
#### Modulos de Pygame #########

juegos=0
#############################

    
imagenes_cartas = dict()

for tuplacarta, archivo in IMAGENES_CARTAS.items():
    imagen = pygame.image.load("img/"+archivo).convert_alpha()
    if imagen.get_size() != (54, 100):
        imagen = pygame.transform.scale(imagen, (54, 100))
    if tuplacarta[1]=="MAZO":
        imagen = pygame.transform.scale(imagen, (81, 150))
    if tuplacarta[1]=="PASO":
        imagen = pygame.transform.scale(imagen, (100, 100))
    if tuplacarta[1]=="CICLOTRAMPA":
        imagen = pygame.transform.scale(imagen,(150,150))
    if tuplacarta[1]=="PENSANDO":
        imagen = pygame.transform.scale(imagen,(100,100))
        
    imagenes_cartas[tuplacarta] = imagen
####################################
    

pygame.display.flip()
ENDGAME=False
robar= True
pasar= False
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
    corriendo=True            
    anotherone=0
    while corriendo:
        if anotherone==1:
            break
        
################################################# Turno Jugador ########################################################################
        if turno%2==0:
            dibujar(mano_jugador,mano_bot,imagenes_cartas,screen,cem)
    
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    corriendo = False
                    ENDGAME=True
                if evento.type == KEYDOWN and evento.key == K_ESCAPE:
                    corriendo = False
                    ENDGAME=True
                if evento.type == MOUSEBUTTONDOWN:
                    p_m=pygame.mouse.get_pos() #p_m = posicion_mouse
                    print p_m[0],p_m[1]
                    if p_m[0]>=700 and p_m[0]<=781 and p_m[1]>=237 and p_m[1]<=387:
                        if robar:
                            mano_jugador,mazo=carta_aleatoria(mano_jugador,mazo)
                            robar = False
                            pasar = True
                            
                    elif p_m[0]>=10 and p_m[0]<=110 and p_m[1]>=262 and p_m[1]<=362:
                        if pasar:
                            turno+=1
                            pygame.display.flip()
                            robar= True
                            pasar= False
                            break
                    else:
                        xmin=4; xmax=58     #coordenadas que ocupa cada carta
                        ymin=414; ymax=514
                        for carta in mano_jugador:
                            if xmax>850:
                                xmin=4; xmax=58
                                ymin=524; ymax=624
                            if p_m[0]>=xmin and p_m[0]<=xmax and p_m[1]>=ymin and p_m[1]<=ymax:
                                print p_m[0]>xmin,p_m[0]<xmax
                                jugada_legalizada=comprobar_jug(carta,cem)
                                if jugada_legalizada[0]==True:
                                    mano_jugador.remove(carta)
                                    dibujar(mano_jugador,mano_bot,imagenes_cartas,screen,cem)
                                    turno,mano_bot,mano_jugador,cem,mazo=comprobar_efecto(jugada_legalizada[1],mano_bot,mano_jugador,turno,carta,cem,mazo,imagenes_cartas,screen)
                                    if len(mano_jugador)==0:
                                        anotherone=1
                                        pygame.display.flip()
                                        robar= True
                                        pasar= False
                                        break
                                    else:
                                        turno+=1
                                        pygame.display.flip()
                                        robar= True
                                        pasar= False
                                        break
                                elif jugada_legalizada[0]==False:
                                    if len(mazo)<2:
                                        mazo,cem=revolver_el_mazo(mazo,cem)        
                                    mano_jugador,mazo=carta_aleatoria(mano_jugador,mazo)
                                    mano_jugador,mazo=carta_aleatoria(mano_jugador,mazo)
                                    turno+=1                
                                    pygame.display.flip()
                                    robar= True
                                    pasar= False
                                    break
                            xmin+=56;xmax+=56  
################################################# Turno UnoBot ########################################################################
        elif turno%2==1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    ENDGAME=True
                pygame.display.flip()      
            while True:
                print "---------Inicio turno UnoBot-------------"
                dibujar(mano_jugador,mano_bot,imagenes_cartas,screen,cem)
                screen.blit(imagenes_cartas[("N","PENSANDO")],(350,20))    
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
                                                            
                            dibujar(mano_jugador,mano_bot,imagenes_cartas,screen,cem)
                                                            
                            if len(mano_bot)==0:
                                anotherone=1
                                print "---------UnoBot ha ganado la partida-------------\n"
                                break
                            
                            turno,mano_bot,mano_jugador,cem,mazo=comprobar_efecto(jugada_legalizada[1],mano_bot,mano_jugador,turno,mejor_carta,cem,mazo,imagenes_cartas,screen)
                            
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
