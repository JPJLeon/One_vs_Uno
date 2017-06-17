
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
        a=((tamano_lista+tamano_lista_trampa)*ctb*cr1)/(crb)-len(manofinal)*crb 
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
        a=((tamano_lista+tamano_lista_trampa)*ct1*crb)/(cr1)-len(manofinal)*cr1
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










