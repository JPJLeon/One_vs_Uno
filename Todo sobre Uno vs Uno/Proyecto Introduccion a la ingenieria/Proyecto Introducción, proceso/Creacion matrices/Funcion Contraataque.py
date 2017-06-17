

def contra_ataque(carta_trampa_jugada,turno,contador_rob_bot,contador_tir_bot,contador_rob_1,contador_tir_1):
        
        #print "---------Iniciando ciclo de trampa-------------"
        color,numero=carta_trampa_jugada
        numero_a_robar=int(numero)
        booleano=0
        while booleano==0:
############################################ UnoBotDos ##########################################################
                if turno%2==1:
                        while True:
                                #print "UnoBotUno ha lanzado una carta trampa: ",carta_trampa_jugada
                                cartas_en_mano=juga2
                                mejor_carta=0
                                mejor_puntuacion=0
                                #
                                #opciones=checkear_jugada_dicc(str(carta_trampa_jugada)+'T')
                                #for color_mano,tipo_mano in cartas_en_mano:
                                #                if (color_mano,tipo_mano)in opciones:
                                #                        if int(opciones[(color_mano,tipo_mano)])>=mejor_puntuacion:
                                #                                
                                #                                
                                #                                mejor_carta=(color_mano,tipo_mano)
                                #                                mejor_puntuacion=int(diccionario_de_opciones[(color_mano,tipo_mano)])
                                #if mejor_carta==0:
                                #       for i in range(numero_a_robar):
                                #               if len(mazoor)==0:
                                #                       revolver_el_mazo()
                                #               carta_aleatoria(juga2)
                                #               contadr_rob_bot+=1
                                #               booleano=1                                     
                                #               break
                                #else:
                                #       jugada_contra_ataque=mejor_carta
                                #       if jugada_contra_ataque[1]==carta_trampa_jugada[1] or jugada_contra_ataque[1]=='+4':
                                #               cartas_en_mano.remove(jugada_contra_ataque)
                                #               lista_trampa_2.append((cem[-1],jugada_contra_ataque))
                                #               contador_tir_bot+=1
                                #               if jugada_contra_ataque[0]=='N':
                                #                       Y=0
                                #                       G=0
                                #                       B=0
                                #                       R=0
                                #                       for cc,_ in juga2:
                                #                               if cc=='Y':
                                #                                       Y+=1
                                #                               if cc=='B':
                                #                                       B+=1
                                #                               if cc=='G':
                                #                                       G+=1
                                #                               if cc=='R':
                                #                                       R+=1
                                #                       Dicc={}
                                #                       Dicc[Y]='Y'
                                #                       Dicc[G]='G'
                                #                       Dicc[B]='B'
                                #                       Dicc[R]='R'
                                #                       color_contra_ataque=Dicc[max(Y,G,B,R)]
                                #                       cem.append(color_contra_ataque,jugada_contra_ataque[1])
                                #                       carta_trampa_jugada=(color_contra_ataque,jugada_contra_ataque[1])
                                #               if jugada_contra_ataque[0]!='N':
                                #                       cem.append(color_contra_ataque,jugada_contra_ataque[1])
                                #                       carta_trampa_jugada=jugada_contra_ataque
                                #
                                #               numero=jugada_contra_ataque[1]
                                #               numero_a_robar+=int(jugada_contra_ataque[1])
                                #               turno+=1
                                #               break
                                #       else:
                                #               lista_trampa_2.append((cem[-1],jugada_contra_ataque))
                                #               for i in range(numero_a_robar+2):
                                #                       if len(mazoor)==0:
                                #                          revolver_el_mazo()
                                #                       carta_aleatoria(juga2)
                                #                       contadr_rob_bot+=1
                                #               booleano=1                                     
                                #               break
                                #
                                #
                                #
                                #
                                #
                                #
                                #
                                if numero=='+2':
                                       l=[]
                                       for color_mano,numero_mano in cartas_en_mano:
                                               if numero_mano=='+2':
                                                       l.append((color_mano,numero_mano))
                                       if len(l)!=0:
                                                jugada_contra_ataque=choice(l)
                                                juga2.remove(jugada_contra_ataque)
                                                contador_tir_bot+=1
                                                l2.append((cem[-1],jugada_contra_ataque))
                                                cem.append(jugada_contra_ataque)
                                                numero=jugada_contra_ataque[1]
                                                numero_a_robar+=int(jugada_contra_ataque[1])
                                                carta_trampa_jugada=jugada_contra_ataque
                                                
                                                turno+=1
                                                break
                                
                                       elif ('N','+4') in juga2:
                                               numero='+4'
                                
                                       else:
                                               for i in range(numero_a_robar):
                                                       if len(mazoor)==0:
                                                               revolver_el_mazo()
                                                       carta_aleatoria(juga2)
                                                
                                               booleano=1                                     
                                               break
                                if numero=='+4':
                                       l=[]
                                       for color_mano,numero_mano in cartas_en_mano:
                                               if numero_mano=='+4':
                                                       l.append((color_mano,numero_mano))
                                       if len(l)!=0:
                                               jugada_contra_ataque=choice(l)
                                               juga2.remove(jugada_contra_ataque)
                                               Y=0
                                               G=0
                                               B=0
                                               R=0
                                               for cc,_ in juga2:
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
                                               carta_contra_ataque=(color_contra_ataque,jugada_contra_ataque[1])
                                               l2.append((cem[-1],carta_contra_ataque))
                                               contador_tir_bot+=1
                                               cem.append(carta_contra_ataque)
                                               numero=carta_contra_ataque[1]
                                               numero_a_robar+=int(numero)
                                               carta_trampa_jugada=carta_contra_ataque
                                                
                                               turno+=1
                                               break
                        
                                
                                       else:
                                               for i in range(numero_a_robar):
                                                       if len(mazoor)==0:
                                                               revolver_el_mazo()
                                                       carta_aleatoria(juga2)
                                                       contador_rob_bot+=1
                                                
                                               booleano=1                                     
                                               break
############################################ UnoBotUno ############################################################
                elif turno%2==0:
                        #print "UnoBotDos ha lanzado una carta trampa: ",carta_trampa_jugada
                        cartas_en_mano=juga1
                        while True:
                                
                                if numero=='+2':
                                       l=[]
                                       for color_mano,numero_mano in cartas_en_mano:
                                               if numero_mano=='+2':
                                                       l.append((color_mano,numero_mano))
                                       if len(l)!=0:
                                                jugada_contra_ataque=choice(l)
                                                juga1.remove(jugada_contra_ataque)
                                                contador_tir_1+=1
                                                lista_trampa_1.append((cem[-1],jugada_contra_ataque))
                                                cem.append(jugada_contra_ataque)
                                                numero=jugada_contra_ataque[1]
                                                numero_a_robar+=int(jugada_contra_ataque[1])
                                                carta_trampa_jugada=jugada_contra_ataque
                                                
                                                turno+=1
                                                break
                                
                                       elif ('N','+4') in juga1:
                                               numero='+4'
                                
                                       else:
                                               for i in range(numero_a_robar):
                                                       if len(mazoor)==0:
                                                               revolver_el_mazo()
                                                       carta_aleatoria(juga1)
                                                
                                               booleano=1                                     
                                               break
                                if numero=='+4':
                                       l=[]
                                       for color_mano,numero_mano in cartas_en_mano:
                                               if numero_mano=='+4':
                                                       l.append((color_mano,numero_mano))
                                       if len(l)!=0:
                                               jugada_contra_ataque=choice(l)
                                               juga1.remove(jugada_contra_ataque)
                                               Y=0
                                               G=0
                                               B=0
                                               R=0
                                               for cc,_ in juga1:
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
                                               lista_trampa_1.append((cem[-1],('N','+4')))
                                               contador_tir_1+=1
                                               cem.append((color_contra_ataque,jugada_contra_ataque[1]))
                                               numero=carta_contra_ataque[1]
                                               numero_a_robar+=int(numero)
                                               carta_trampa_jugada=(color_contra_ataque,jugada_contra_ataque[1])
                                                
                                               turno+=1
                                               break
                        
                                
                                       else:
                                               for i in range(numero_a_robar):
                                                       if len(mazoor)==0:
                                                               revolver_el_mazo()
                                                       carta_aleatoria(juga1)
                                                       contador_rob_1+=1
                                                
                                               booleano=1                                     
                                               break
        return turno,contador_rob_bot,contador_tir_bot,contador_rob_1,contador_tir_1
