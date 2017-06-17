def combinaciones(a,b,c):
        comb=list()
        for i in colors:
                for k in num:
                        comb.append((i,k))
        return comb+c

num=('0','1','2','3','4','5','6','7','8','9',"+2","REV","SKIP")
colors=("Y","B","G","R")
specials=[("N","+4"),("N","+4"),("N","+4"),("N","+4"),("N","CC"),("N","CC"),("N","CC"),("N","CC")]
mazo=combinaciones(colors,num,specials)
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
    archivo.close()            
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

def obtener_puntuacion_bot(lista,manofinal,ct1,ctb,cr1,crb):
        tamaño_lista=len(lista)
        a=(tamaño_lista*ctb*cr1)/(crb*ct1) -len(manofinal)
        return a

def modificar_archivos(lista,puntaje):
        for carta1,carta2 in lista:
                color2,tipo2=carta2
                listag=checkear_jugada_list(carta1)
                for elemento in listag:
                        if color2 in elemento and tipo2 in elemento:
                                elementos[2]=int(elemento[2])+puntaje
                for i in range(len(listag)):
                        listag[i]=';'.join(listag[i])
                listag=' '.join(listag)
                archivo=open(str(carta1)+'.txt','w')
                archivo.write(listag)
                archivo.close()
                        











        
