"""
nombre: indiceNumero
entrada: numero e indice
restriccion: que sea recursivo,entero,mayor a 0
salida: el indice
"""
def indiceNumero(num,indice):
    if num<0:
        num*=-1
    if not (num,int):
        return "Debe ingresar un numero"
    l1=largo(num)
    l2=largo(indice)
    if l2<l1:
        contador=l1-1
        return indice2(num,indice,contador)
    
    else:
        return "Error el indice solicitado exede el largo del numero"

   
def indice2(num,indice,contador):
    if contador==indice:
        return num%10
    else:
        
        return indice2(num//10,indice,contador-1)#voltear numero
    
def largo(x):
    if x==0:
        return 0
    else:
        return 1+largo(x//10)

"""
nombre:cortarNumero
entrada:num,fin,inicio
salida:num cortado
restricciones : no exceden largos,entero"""

def cortarNumero(num,inicio,fin):
    if not(fin,int):
        return "El final debe ser un entero"
    if not(inicio,int):
        return "El inicion debe ser entero"
    if not(num,int):
        return "El numero debe ser entero"
    l1=largo (num)
    l2=largo(inicio)
    l3=largo(fin)

    if not l1>=l2:
        return "el inico debe ser menor al largo de el numero"
    if not l3<l1:
        return "el final debe ser menor al largo del numero"
    cont=l1-1
    r=0
    return cut2(num,inicio,fin,cont,r)

def cut2(num,inicio,fin,cont,r):
    if cont==inicio:
        r+=1
        modulo=10**r
        return num%modulo
    elif cont<=fin:
        r+=1
        return cut2(num,inicio,fin,cont-1,r)
    else:
         return cut2(num//10,inicio,fin,cont-1,r)



"""
nombre: listaCapicua
entrada:lista
salida true false
restricciones: que sea lista
"""

def listaCapicua(lista):
    if not (lista,list):
        return "debe ingresar una lista"
    indice1=0
    indice2=-1
    contador=indice2*-1
    return lista2(lista,indice1,indice2,)

def lista2(lista,indice1,indice2,):
    if lista==[]:
        return True
    else:
        if lista[indice1]==lista[indice2]:
            return lista2(lista[1:-1],indice1,indice2)

        else:
 