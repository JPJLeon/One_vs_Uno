
import random

#############################################################################

def revolver_el_mazo():
        for i in range(len(cem)):
                if cem[-1]!=cem[i]:
                        if cem[i][1]=="+4" or cem[i][1]=="CC":
                                mazoor.append(("N",cem[i][1]))
                        else:
                                mazoor.append(cem[i])
                        cem.remove(cem[i])
                        
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
                                cartas=random.choice(a)
                                baraja1.append(cartas)
                                a.remove(cartas)
                if i==1:
                        for l in range(8):
                                cartas2=random.choice(a)
                                baraja2.append(cartas2)
                                a.remove(cartas2)
        while True:
                c,n=random.choice(a)
                if n in ['0','1','2','3','4','5','6','7','8','9']:
                        car=(c,n)
                        a.remove(car)
                        break
        cem.append(car)
        return (a,baraja1,baraja2)

#############################################################################

def carta_aleatoria(a): #Robar una carta, quitarla del mazo y ponerla en la mano
        carta=random.choice(mazoor)
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

def contra_ataque(carta_trampa_jugada,turno):
        print "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
        print "---------Iniciando ciclo de trampa-------------"
        color,numero=carta_trampa_jugada
        numero_a_robar=int(numero)
        booleano=0
        while booleano==0:
                if turno%2==1:
                        print "El Jugador 1 ha lanzado una carta trampa: ",carta_trampa_jugada
                        while True:
                                print ""
                                print "Cartas en mano: ",juga2
                                print ""
                                jugada_contra_ataque=raw_input("Desea lanzar una carta trampa como respuesta?(Si=S; No=N): ")
                                
                                if jugada_contra_ataque=="S":
                                        print ""
                                        
                                        color_contra_ataque=raw_input("Ingrese el color de su carta: ")
                                        tipo_contra_ataque=(raw_input("Ingrese el tipo de su carta: "))
                                        carta_contra_ataque=tuple((color_contra_ataque,tipo_contra_ataque))
                                        
                                        if tipo_contra_ataque>=numero and carta_contra_ataque in juga2 and (tipo_contra_ataque=="+2" or tipo_contra_ataque=="+4"):
                                                juga2.remove(carta_contra_ataque)
                                                
                                                if tipo_contra_ataque=="+4":
                                                        color_contra_ataque=raw_input("Que color eliges? (Y= AMARILLO, B= AZUL,R= ROJO,G= VERDE): ")
                                                        
                                                carta_contra_ataque=tuple((color_contra_ataque,tipo_contra_ataque))
                                                cem.append(carta_contra_ataque)
                                                
                                                numero=tipo_contra_ataque
                                                numero_a_robar+=int(tipo_contra_ataque)
                                                carta_trampa_jugada=carta_contra_ataque
                                                
                                                turno+=1
                                                print "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                                                break
                                        
                                        else:
                                                print "Jugada invalida, aplicando penalizacion."
                                                for i in range(numero_a_robar+2):
                                                        if len(mazoor)==0:
                                                                revolver_el_mazo()
                                                        carta_aleatoria(juga2)
                                                
                                                booleano=1
                                                break
                                                
                                elif jugada_contra_ataque=="N":
                                        for i in range(numero_a_robar):
                                                if len(mazoor)==0:
                                                        revolver_el_mazo()
                                                carta_aleatoria(juga2)
                                                
                                        booleano=1                                     
                                        break
                elif turno%2==0:
                        print "El Jugador 2 ha lanzado una carta trampa: ",carta_trampa_jugada
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
                                                cem.append(carta_contra_ataque)
                                                
                                                numero=tipo_contra_ataque
                                                numero_a_robar+=int(tipo_contra_ataque)
                                                carta_trampa_jugada=carta_contra_ataque
                                                turno+=1
                                                print "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                                                break
                                        
                                        else:
                                                print "Jugada invalida, aplicando penalizacion."
                                                for i in range(numero_a_robar+2):
                                                        if len(mazoor)==0:
                                                                revolver_el_mazo()
                                                        carta_aleatoria(juga1)
                                                        
                                                booleano=1
                                                break
                                                
                                elif jugada_contra_ataque=="N":
                                        for i in range(numero_a_robar):
                                                if len(mazoor)==0:
                                                        revolver_el_mazo()
                                                carta_aleatoria(juga1)
                                                
                                        booleano=1
                                        break
        return turno
#############################################################################
        
def comprobar_efecto(efect,mano,turno,jugada): #Comprueba el efecto y cambia las manos correspondientes
        if efect == "SKIP" or efect == "REV":
                cem.append(jugada)
                turno +=1
                return turno
        if efect == "+2":
                cem.append(jugada)
                turno +=1
                turno=contra_ataque(jugada,turno)
                return turno
        if efect == "+4":
                
                pregunta = raw_input("Que color eliges? (Y= AMARILLO, B= AZUL,R= ROJO,G= VERDE): ")
                jugada=tuple((pregunta,jugada[1]))
                cem.append(jugada)
                turno +=1
                turno=contra_ataque(jugada,turno)
                return turno
                
                
        if efect == "CC":
                pregunta = raw_input("Que color eliges? (Y= AMARILLO, B= AZUL,R= ROJO,G= VERDE): ")
                jugada= (pregunta,jugada[1])
                cem.append(jugada)
                return turno
        cem.append(jugada)
        return turno
        
#############################################################################
                        
num=('0','1','2','3','4','5','6','7','8','9',"+2","REV","SKIP")
colors=("Y","B","G","R")
specials=[("N","+4"),("N","+4"),("N","+4"),("N","+4"),("N","CC"),("N","CC"),("N","CC"),("N","CC")]
mazo=combinaciones(colors,num,specials)
while True:
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
                                print "---------Inicio turno jugador 1-------------"
                                print ""
                                print("La carta actual es: "),cem[-1]
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
                                        print "Ha robado la carta: ",juga1[-1]
                                        print ""
                                        print("Tus cartas son: "),juga1
                                        print ""
                                        jugada1=raw_input("Que desea hacer?(P=PASAR,B=BOTAR): ")
                                        if jugada1=="P":
                                                turno+=1
                                                print "---------Fin turno jugador 1-------------"
                                                print "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                                                break
                                        
                                if jugada1=="B":
                                        color111=raw_input("Ingrese el color de su carta: ")
                                        tipo111=(raw_input("Ingrese el tipo de su carta: "))
                                        jugada111=tuple((color111,tipo111))
                                        jugadia=comprobar_jug(jugada111)
                                        if jugadia[0]==True:
                                                juga1.remove(jugada111)
                                                turno=comprobar_efecto(jugadia[1],juga2,turno,jugada111)
                                                
                                                print "La carta jugada fue",jugada111
                                                if len(juga1)==0:
                                                        anotherone=1
                                                        print "---------Fin turno jugador 1-------------"
                                                        print "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                                                        break
                                                else:
                                                        turno+=1
                                                        print "---------Fin turno jugador 1-------------"
                                                        print "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                                                        break
                                        elif jugadia[0]==False:
                                                carta_aleatoria(juga1)
                                                carta_aleatoria(juga1)
                                                turno+=1
                                                print "---------Fin turno jugador 1-------------"
                                                print "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                                                break
                                                
################################################# Turno Player2 ########################################################################
                elif turno%2==1:
                        while True:
                                print "---------Inicio turno jugador 2-------------"
                                print ""
                                print("La carta actual es: "),cem[-1]
                                print ""
                                
                                if len(mazoor)==0:
                                        revolver_el_mazo()
                                        
                                print("Tus cartas son: "),juga2
                                print ""
                                jugada1=0
                                while jugada1!="R" and jugada1!="B":
                                        jugada1=raw_input("Que desea hacer?(R=ROBAR,B=BOTAR): ")
                                        
                                if jugada1=="R":
                                        carta_aleatoria(juga2)
                                        print "Ha robado la carta: ",juga2[-1]
                                        print ""
                                        print("Tus cartas son: "),juga2
                                        print ""
                                        jugada1=raw_input("Que desea hacer?(P=PASAR,B=BOTAR): ")
                                        if jugada1=="P":
                                                turno+=1
                                                print "---------Fin turno jugador 2-------------"
                                                print "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                                                break
                                        
                                if jugada1=="B":
                                        color111=raw_input("Ingrese el color de su carta: ")
                                        tipo111=(raw_input("Ingrese el tipo de su carta: "))
                                        jugada111=tuple((color111,tipo111))
                                        jugadia=comprobar_jug(jugada111)
                                        if jugadia[0]==True:
                                                juga2.remove(jugada111)
                                                turno=comprobar_efecto(jugadia[1],juga1,turno,jugada111)
                                                
                                                print "La carta jugada fue",jugada111
                                                if len(juga2)==0:
                                                        anotherone=1
                                                        print "---------Fin turno jugador 2-------------"
                                                        print "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                                                        break
                                                else:
                                                        turno+=1
                                                        print "---------Fin turno jugador 2-------------"
                                                        print "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                                                        break
                                        elif jugadia[0]==False:
                                                carta_aleatoria(juga2)
                                                carta_aleatoria(juga2)
                                                turno+=1
                                                print "---------Fin turno jugador 2-------------"
                                                print "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                                                break
                                
                

















                                                       
