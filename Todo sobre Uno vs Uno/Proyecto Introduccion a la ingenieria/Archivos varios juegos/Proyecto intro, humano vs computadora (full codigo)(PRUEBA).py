from random import *

#############################################################################

def revolver_el_mazo():
        for i in range(len(cem)-1):
                if cem[0][1]=="+4" or cem[0][1]=="CC":
                        mazoor.append(("N",cem[0][1]))
                else:
                        mazoor.append(cem[0])
                cem.remove(cem[0])
                        
#############################################################################
                        
def combinaciones(a,b,c):
        comb=list()
        for i in colors:
                for k in num:
                        comb.append((i,k))
        return comb+c

#############################################################################

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

#############################################################################

def carta_aleatoria(a): #Robar una carta, quitarla del mazo y ponerla en la mano
        carta=choice(mazoor)
        a.append(carta)
        mazoor.remove(carta)

#############################################################################
        
def comprobar_jug(a): #Comprobar que carta se jugo, si es legal y si tiene algun efecto en la partida
        b,c=a
        col,num=cem[-1]
        if b == col or c == num or b == "N":
                        return (True,c)
        else:
                return (False,1)
#############################################################################

def contra_ataque(carta_trampa_jugada,turno,contador_rob_bot,contador_tir_bot,contador_rob_1,contador_tir_1):
        
        print "---------Iniciando ciclo de trampa-------------"
        color,numero=carta_trampa_jugada
        numero_a_robar=int(numero)
        booleano=0
        while booleano==0:
                if turno%2==1:
                        while True:
                                cartas_en_mano=juga2
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
                                              
                elif turno%2==0:
                        print "UnoBot ha lanzado una carta trampa: ",carta_trampa_jugada
                        while True:
                                print ""
                                print "Cartas en mano: ",juga1
                                print ""
                                jugada_contra_ataque=raw_input("Desea lanzar una carta trampa como respuesta?(Si=S; No=N): ")
                                
                                if jugada_contra_ataque=="S":
                                        print ""
                                        
                                        color_contra_ataque=raw_input("Ingrese el color de su carta: ")
                                        tipo_contra_ataque=(raw_input("Ingrese el tipo de su carta: "))
                                        carta_contra_ataque=tuple((color_contra_ataque,tipo_contra_ataque))
                                        
                                        if tipo_contra_ataque>=numero and carta_contra_ataque in juga1 and (tipo_contra_ataque=="+2" or tipo_contra_ataque=="+4"):
                                                juga1.remove(carta_contra_ataque)
                                                
                                                if tipo_contra_ataque=="+4":
                                                        color_contra_ataque=raw_input("Que color eliges? (Y= AMARILLO, B= AZUL,R= ROJO,G= VERDE): ")
                                                        
                                                carta_contra_ataque=tuple((color_contra_ataque,tipo_contra_ataque))
                                                l1.append((cem[-1],carta_contra_ataque))
                                                cem.append(carta_contra_ataque)
                                                contador_tir_1+=1
                                                numero=tipo_contra_ataque
                                                numero_a_robar+=int(tipo_contra_ataque)
                                                carta_trampa_jugada=carta_contra_ataque
                                                turno+=1
                                                
                                                break
                                        
                                        else:
                                                print "Jugada invalida, aplicando penalizacion."
                                                for i in range(numero_a_robar+2):
                                                        if len(mazoor)==0:
                                                                revolver_el_mazo()
                                                        carta_aleatoria(juga1)
                                                        contador_rob_1+=1
                                                        
                                                booleano=1
                                                break
                                                
                                elif jugada_contra_ataque=="N":
                                        for i in range(numero_a_robar):
                                                if len(mazoor)==0:
                                                        revolver_el_mazo()
                                                carta_aleatoria(juga1)
                                                contador_rob_1+=1
                                                
                                        booleano=1
                                        break
        return turno,contador_rob_bot,contador_tir_bot,contador_rob_1,contador_tir_1
#############################################################################
        
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
                        pregunta = raw_input("Que color eliges? (Y= AMARILLO, B= AZUL,R= ROJO,G= VERDE): ")
                        jugada=tuple((pregunta,jugada[1]))
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
                        pregunta = raw_input("Que color eliges? (Y= AMARILLO, B= AZUL,R= ROJO,G= VERDE): ")
                        jugada= (pregunta,jugada[1])
                        cem.append(jugada)
                        return turno,crb,ctb,cr1,ct1
        cem.append(jugada)
        return turno,crb,ctb,cr1,ct1
#############################################################################

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

#############################################################################    

def checkear_jugada_dicc(carta):
    archivo=open(str(carta)+'.txt')
    diccionario={}
    for linea in archivo:
        linea=linea.split(" ")
        for elemento in linea:
                elemento=elemento.split(';')
                diccionario[tuple((elemento[0],elemento[1]))]=elemento[2]
    return diccionario
#############################################################################
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
#############################################################################
def obtener_puntuacion_bot(lista,manofinal,ct1,ctb,cr1,crb):
        tamano_lista=len(lista)
        if ct1==0:
                ct1=1
        if ctb==0:
                ctb=1
        if cr1==0:
                cr1=1
        if crb==0:
                crb=1
        a=(tamano_lista*ctb*cr1)/(crb*ct1)-len(manofinal)
        return a
#############################################################################
def obtener_puntuacion_jug(lista,manofinal,ct1,ctb,cr1,crb):
        tamano_lista=len(lista)
        if ct1==0:
                ct1=1
        if ctb==0:
                ctb=1
        if cr1==0:
                cr1=1
        if crb==0:
                crb=1
        a=(tamano_lista*ct1*crb)/(cr1*ctb)-len(manofinal)
        return a
#############################################################################
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
#############################################################################                        
num=('0','1','2','3','4','5','6','7','8','9',"+2","REV","SKIP")
colors=("Y","B","G","R")
specials=[("N","+4"),("N","+4"),("N","+4"),("N","+4"),("N","CC"),("N","CC"),("N","CC"),("N","CC")]
mazo=combinaciones(colors,num,specials)
while True:
        l1=[]
        l2=[]
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
                        
                    
################################################# Turno Player1 ########################################################################
                if turno%2==0:
                        while True:
                                print "---------Inicio turno Jugador-------------"
                                print ""
                                print("La carta actual es: "),cem[-1]
                                print ""
                                print "A UnoBot le quedan",len(juga2),"cartas en la mano"
                                print ""
                                if len(mazoor)==0:
                                        revolver_el_mazo()
                                        
                                print("Tus cartas son: "),juga1
                                print ""
                                jugada1=0
                                while jugada1!="R" and jugada1!="B":
                                        jugada1=raw_input("Que desea hacer?(R=ROBAR,B=BOTAR): ")
                                        
                                if jugada1=="R":
                                        carta_aleatoria(juga1)
                                        contador_rob_1+=1
                                        print "Ha robado la carta: ",juga1[-1]
                                        print ""
                                        print("Tus cartas son: "),juga1
                                        print ""
                                        jugada1=raw_input("Que desea hacer?(P=PASAR,B=BOTAR): ")
                                        if jugada1=="P":
                                                turno+=1
                                                print "---------Fin turno Jugador-------------"
                                                print "\n\n\n"
                                                break
                                        
                                if jugada1=="B":
                                        color111=raw_input("Ingrese el color de su carta: ")
                                        tipo111=(raw_input("Ingrese el tipo de su carta: "))
                                        jugada111=tuple((color111,tipo111))
                                        jugadia=comprobar_jug(jugada111)
                                        if jugadia[0]==True:
                                                juga1.remove(jugada111)
                                                l1.append((cem[-1],jugada111))
                                                contador_tir_1+=1
                                                turno,contador_rob_bot,contador_tir_bot,contador_rob_1,contador_tir_1=comprobar_efecto(jugadia[1],juga2,turno,jugada111,contador_rob_bot,contador_tir_bot,contador_rob_1,contador_tir_1)
                                                
                                                
                                                if len(juga1)==0:
                                                        anotherone=1
                                                        print "---------Jugador ha ganado la partida-------------"
                                                        print "\n\n\n"
                                                        break
                                                else:
                                                        turno+=1
                                                        print "---------Fin turno Jugador-------------"
                                                        print "\n\n\n"
                                                        break
                                        elif jugadia[0]==False:
                                                carta_aleatoria(juga1)
                                                carta_aleatoria(juga1)
                                                contador_rob_1+=2
                                                turno+=1
                                                print "---------Fin turno jugador 1-------------"
                                                print "\n\n\n"
                                                break
                                                
################################################# Turno Computadora ########################################################################
                elif turno%2==1:
                        
                        
                                
                print "\n\n\n\n\n"
        print l1
        print l2
        puntosb=obtener_puntuacion_bot(l2,juga2,contador_tir_1,contador_tir_bot,contador_rob_1,contador_rob_bot)
        puntosj=obtener_puntuacion_jug(l1,juga1,contador_tir_1,contador_tir_bot,contador_rob_1,contador_rob_bot)
        print "\n Puntuacion bot:",puntosb
        print "\n Puntuacion jugador:",puntosj
        modificar_archivos(l1,puntosj)
        modificar_archivos(l2,puntosb)














                                                       

