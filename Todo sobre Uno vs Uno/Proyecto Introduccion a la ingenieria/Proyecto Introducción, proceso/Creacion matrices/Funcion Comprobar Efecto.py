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
