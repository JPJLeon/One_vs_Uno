from random import *

def revolver_el_mazo():
        for i in range(len(cem)-1):
                if cem[0][1]=="+4" or cem[0][1]=="CC":
                        mazoor.append(("N",cem[0][1]))
                else:
                        mazoor.append(cem[0])
                cem.remove(cem[0])
                              
                       
def combinaciones(a,b,c):
        comb=list()
        for i in colors:
                for k in num:
                        comb.append((i,k))
        return comb+c



def reparto(a): #funcion que da al inicio 8 cartas a cada jugador y deja una carta en el cementeterio
        baraja1=[]
        baraja2=[]
        for i in range(2):
                if i==0:
                        for k in range(8):
                                cartas=choice(a)
                                baraja1.append(cartas)
                                a.remove(cartas)
                if i==1:
                        for l in range(8):
                                cartas2=choice(a)
                                baraja2.append(cartas2)
                                a.remove(cartas2)
        while True:
                c,n=choice(a)
                if n in ['0','1','2','3','4','5','6','7','8','9']:
                        car=(c,n)
                        a.remove(car)
                        break
        cem.append(car)
        return (a,baraja1,baraja2)



def carta_aleatoria(a): #Robar una carta, quitarla del mazo y ponerla en la mano
        carta=choice(mazoor)
        a.append(carta)
        mazoor.remove(carta)


          
def comprobar_jug(a): #Comprobar que carta se jugo, si es legal y si tiene algun efecto en la partida
        b,c=a
        col,num=cem[-1]
        if b == col or c == num or b == "N":
                return (True,c)
        else:
                return (False,1)


def crear_archivos_matriz():
        for elemento in mazo:
                if elemento!=("N","+4") and elemento!=("N","CC"):
                        archivo=open((str(elemento)+".txt"),'w')
                        l=set()
                        for color,tipo in mazo:
                                if color==elemento[0] or tipo==elemento[1]:
                                        if tuple((color,tipo))!=elemento:
                                                a=str(color)+';'+str(tipo)+';0'
                                                l.add(a)
                                                b='N'+';'+'CC'+';0'
                                                l.add(b)
                                                b='N'+';'+'+4'+';0'
                                                l.add(b)
                        archivo.write(" ".join(l))
                        archivo.close()
                else:
                        archivo=open((str(elemento)+".txt"),'w')
                        l=set()
                        for color,tipo in mazo:
                                a=str(color)+';'+str(tipo)+';0'
                                l.add(a)
                                b='N'+';'+'CC'+';0'
                                l.add(b)
                                b='N'+';'+'+4'+';0'
                                l.add(b)
                        archivo.write(" ".join(l))
                        archivo.close()
        return mazo



def checkear_jugada_dicc(carta):
        archivo=open(str(carta)+'.txt')
        diccionario={}
        for linea in archivo:
                linea=linea.split(" ")
                for elemento in linea:
                        elemento=elemento.split(';')
                        diccionario[tuple((elemento[0],elemento[1]))]=elemento[2]
        return diccionario



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


def obtener_puntuacion_bot(lista,manofinal,ct1,ctb,cr1,crb,lista_trampa):
        tamano_lista=len(lista)
        tamano_lista_trampa=len(lista_trampa)
        if ct1==0:
                ct1=1
        if ctb==0:
                ctb=1
        if cr1==0:
                cr1=1
        if crb==0:
                crb=1
        a=((tamano_lista+tamano_lista_trampa)*cr1)/(crb)-len(manofinal)
        return a


def obtener_puntuacion_jug(lista,manofinal,ct1,ctb,cr1,crb,lista_trampa):
        tamano_lista=len(lista)
        tamano_lista_trampa=len(lista_trampa)
        if ct1==0:
                ct1=1
        if ctb==0:
                ctb=1
        if cr1==0:
                cr1=1
        if crb==0:
                crb=1
        a=((tamano_lista+tamano_lista_trampa)*crb)/(cr1)-len(manofinal)
        return a


def modificar_archivos(lista,puntaje):
        for carta1,carta2 in lista:
                
                color2,tipo2=carta2
                listag=checkear_jugada_list(carta1)
                for elemento in listag:
                        if color2 in elemento and tipo2 in elemento:
                                elemento[2]=str(int(elemento[2])+puntaje)
                for i in range(len(listag)):
                        listag[i]=';'.join(listag[i])
                listag=' '.join(listag)
                archivo=open(str(carta1)+'.txt','w')
                archivo.write(listag)
                archivo.close()
def modificar_archivos_trampas(lista,puntaje):
        for carta1,carta2 in lista:
                color2,tipo2=carta2
                listag=checkear_jugada_list(str(carta1)+'T')
                for elemento in listag:
                        if color2 in elemento and tipo2 in elemento:
                                elemento[2]=str(int(elemento[2])+puntaje)
                for i in range(len(listag)):
                        listag[i]=';'.join(listag[i])
                listag=' '.join(listag)
                archivo=open(str(carta1)+'T.txt','w')
                archivo.write(listag)
                archivo.close()

################################################################################################################################
################################################################################################################################



def contra_ataque(carta_trampa_jugada,turno,contador_rob_bot,contador_tir_bot,contador_rob_1,contador_tir_1):
          
        #print "---------Iniciando ciclo de trampa-------------"
        color,numero=carta_trampa_jugada
        numero_a_robar=int(numero)
        booleano=0
        while booleano==0:
############################################ UnoBotDos ##########################################################
                if turno%2==1:
                        
                        #print "UnoBotUno ha lanzado una carta trampa: ",carta_trampa_jugada
                        cartas_en_mano=juga2
                        while True:
                                
                                mejor_carta=0
                                mejor_puntuacion=0
                                        
                                opciones=checkear_jugada_dicc(str(carta_trampa_jugada)+'T')
                                for color_mano,tipo_mano in cartas_en_mano:
                                        if (color_mano,tipo_mano)in opciones:
                                                if int(opciones[(color_mano,tipo_mano)])>=mejor_puntuacion:
                                                        mejor_carta=(color_mano,tipo_mano)
                                                        mejor_puntuacion=int(diccionario_de_opciones[(color_mano,tipo_mano)])
                                if mejor_carta==0:
                                        for i in range(numero_a_robar):
                                                if len(mazoor)==0:
                                                        revolver_el_mazo()
                                                if len(juga2)<70:
                                                        carta_aleatoria(juga2)
                                                        contador_rob_bot+=1
                                        booleano=1                                     
                                        break
                                else:
                                        jugada_contra_ataque=mejor_carta
                                        if jugada_contra_ataque[1]==carta_trampa_jugada[1] or jugada_contra_ataque[1]=='+4':
                                                juga2.remove(jugada_contra_ataque)
                                                lista_trampa_2.append((cem[-1],jugada_contra_ataque))
                                                contador_tir_bot+=1
                                                if jugada_contra_ataque[0]=='N':
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
                                                        cem.append((color_contra_ataque,jugada_contra_ataque[1]))
                                                        carta_trampa_jugada=(color_contra_ataque,jugada_contra_ataque[1])
                                                        if jugada_contra_ataque[0]!='N':
                                                                cem.append(jugada_contra_ataque)
                                                                carta_trampa_jugada=jugada_contra_ataque
                                        
                                                        numero=jugada_contra_ataque[1]
                                                        numero_a_robar+=int(jugada_contra_ataque[1])
                                                        turno+=1
                                                        break
                                        else:
                                                print "------------UnoBotDos se ha equivocado----------"
                                                print "jugada de UnoBotDos: ",jugada_contra_ataque, "carta en cementerio:",cem[-1]
                                                lista_trampa_2.append((cem[-1],jugada_contra_ataque))
                                                for i in range(numero_a_robar+2):
                                                        if len(mazoor)<=1:
                                                                revolver_el_mazo()
                                                        if len(juga2)<70:
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
                                                numero=jugada_contra_ataque[1]
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
        


################################################################################################################################
################################################################################################################################

def comprobar_efecto(efect,mano,turno,jugada,crb,ctb,cr1,ct1): #Comprueba el efecto y cambia las manos correspondientes
        
        if efect == "SKIP" or efect == "REV":
                cem.append(jugada)
                turno +=1
                
                return turno,crb,ctb,cr1,ct1
        if efect == "+2":
                
                cem.append(jugada)
                turno +=1
                turno,crb,ctb,cr1,ct1=contra_ataque(jugada,turno,crb,ctb,cr1,ct1)
                return turno,crb,ctb,cr1,ct1
        if efect == "+4":
                
                if turno%2==1:
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
                        color_elegido=Dicc[max(Y,G,B,R)]
                        jugada=tuple((color_elegido,jugada[1]))
                        cem.append(jugada)
                        turno +=1
                        
                        turno,crb,ctb,cr1,ct1=contra_ataque(jugada,turno,crb,ctb,cr1,ct1)
                        
                        return turno,crb,ctb,cr1,ct1
                              
                else:
                        
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
                        color_elegido=Dicc[max(Y,G,B,R)]
                        jugada=tuple((color_elegido,jugada[1]))
                        cem.append(jugada)
                        turno +=1
                        turno,crb,ctb,cr1,ct1=contra_ataque(jugada,turno,crb,ctb,cr1,ct1)
                        
                        return turno,crb,ctb,cr1,ct1
                    
        if efect == "CC":
                
                if turno%2==1:
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
                        color_elegido=Dicc[max(Y,G,B,R)]
                        jugada=tuple((color_elegido,jugada[1]))
                        cem.append(jugada)
                        return turno,crb,ctb,cr1,ct1
                else:
                        
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
                        color_elegido=Dicc[max(Y,G,B,R)]
                        jugada=tuple((color_elegido,jugada[1]))
                        cem.append(jugada)
                        return turno,crb,ctb,cr1,ct1
        
        cem.append(jugada)
        return turno,crb,ctb,cr1,ct1


################################################################################################################################
################################################################################################################################



juegos=0
while juegos<10:
        juegos+=1
        num=('0','1','2','3','4','5','6','7','8','9',"+2","REV","SKIP",'0','1','2','3','4','5','6','7','8','9',"+2","REV","SKIP")
        colors=("Y","B","G","R")
        specials=[("N","+4"),("N","+4"),("N","+4"),("N","+4"),("N","CC"),("N","CC"),("N","CC"),("N","CC")]
        mazo=combinaciones(colors,num,specials)
        l1=[]
        l2=[]
        lista_trampa_1=[]
        lista_trampa_2=[]
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
                                                                if color_mano==color_actual or tipo_mano==tipo_actual or color_mano=="N":
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
                                                        l1.append((cem[-1],mejor_carta))
                                                        
                                                if len(juga1)==0:
                                                        anotherone=1
                                                        print "---------UnoBotUno ha ganado la partida-------------\n"
                                                        #print "\n\n\n"
                                                        break
                                                turno,contador_rob_bot,contador_tir_bot,contador_rob_1,contador_tir_1=comprobar_efecto(jugadia[1],juga1,turno,mejor_carta,contador_rob_bot,contador_tir_bot,contador_rob_1,contador_tir_1)
                                                            
                                                #print "UnoBot ha jugado la carta",mejor_carta
                                                            
                                                if len(juga1)!=0:
                                                        turno+=1
                                                        #print "---------Fin turno UnoBotUno-------------\n"
                                                        break
                                        elif jugadia[0]==False:
                                                #print "------- UnoBotUno se ha equivocado--------\n"
                                                if len(mazoor)<2:
                                                        revolver_el_mazo()
                                                carta_aleatoria(juga1)
                                                carta_aleatoria(juga1)
                                                turno+=1
                                                #print "---------Fin turno UnoBotUno-------------\n"
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
                                opciones=checkear_jugada_dicc(cem[-1])
                                
                                for color_mano,tipo_mano in cartas_en_mano:
                                        if (color_mano,tipo_mano)in opciones:
                                                if int(opciones[(color_mano,tipo_mano)])>=mejor_puntuacion:                  
                                                        mejor_carta=(color_mano,tipo_mano)
                                                        mejor_puntuacion=int(opciones[(color_mano,tipo_mano)])
                                
                                if mejor_carta==0:
                                        #print "----------- UnoBotDos ha robado una carta-------"
                                        if len(juga2)<70:
                                                carta_aleatoria(juga2)
                                                contador_rob_bot+=1
                                mejor_puntuacion=0
                                mejor_carta=0
                                for color_mano,tipo_mano in cartas_en_mano:
                                        if (color_mano,tipo_mano)in opciones:
                                                if int(opciones[(color_mano,tipo_mano)])>=mejor_puntuacion:
                                                        mejor_carta=(color_mano,tipo_mano)
                                                        mejor_puntuacion=int(diccionario_de_opciones[(color_mano,tipo_mano)])
                                
                                if mejor_carta==0:
                                        #print "--------- UnoBotDos ha pasado el turno-------\n"
                                        turno+=1
                                        break
                                else:
                                        
                                        jugadia=comprobar_jug(mejor_carta)
                                        if jugadia[0]==True:
                                                
                                                juga2.remove(mejor_carta)
                                                contador_tir_bot+=1
                                                l2.append((cem[-1],mejor_carta))
                                                if len(juga2)==0:
                                                        anotherone=1
                                                        print "---------UnoBotDos ha ganado la partida-------------\n"
                                                        break
                                                turno,contador_rob_bot,contador_tir_bot,contador_rob_1,contador_tir_1=comprobar_efecto(jugadia[1],juga1,turno,mejor_carta,contador_rob_bot,contador_tir_bot,contador_rob_1,contador_tir_1)
                                                if len(juga2)!=0:
                                                        turno+=1
                                                        
                                                        break
                                                 
                                        elif jugadia[0]==False:
                                                
                                                #print "------- UnoBotDos se ha equivocado -------\n"
                                                
                                                contador_rob_bot+=2
                                                l2.append((cem[-1],mejor_carta))
                                                if len(mazoor)<2:
                                                        revolver_el_mazo()
                                                if len(juga2)<70:
                                                        carta_aleatoria(juga2)
                                                        carta_aleatoria(juga2)
                                                turno+=1
                                                break
                                        
                                        
                #print "\n\n\n\n\n"
        #puntosb=obtener_puntuacion_bot(l2,juga2,contador_tir_1,contador_tir_bot,contador_rob_1,contador_rob_bot,lista_trampa_2)
        if len(juga1)==0:
                puntosj=obtener_puntuacion_jug(l1,juga1,contador_tir_1,contador_tir_bot,contador_rob_1,contador_rob_bot,lista_trampa_1) 
                puntosb=-1*puntosj
        if len(juga2)==0:
                puntosb=obtener_puntuacion_bot(l2,juga2,contador_tir_1,contador_tir_bot,contador_rob_1,contador_rob_bot,lista_trampa_2)
                puntosj=-1*puntosb
        print "\n Puntuacion UnoBotDos:",puntosb
        print "\n Puntuacion UnoBotUno:",puntosj
        

        modificar_archivos(l1,puntosj)
        modificar_archivos(l2,puntosb)
        modificar_archivos_trampas(lista_trampa_1,puntosj)
        modificar_archivos_trampas(lista_trampa_2,puntosb)
        print "---------------ARCHIVOS MODIFICADOS--------"












                                                                   

