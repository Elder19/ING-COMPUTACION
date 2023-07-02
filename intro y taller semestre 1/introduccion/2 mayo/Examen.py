"""
nombre: lista_par_ligado
entrada: lista
salida true o false
restrcciones: mayor a 0 y int
"""
def lista_par_ligado(lista):
    if isinstance(lista,list):
        if lista!=[]:
            for elemento in lista:
                if elemento>0:
                    if isinstance(elemento,int):
                        continue
                    else:
                        return "error el elemento debe ser int "
                else:
                    return "error el elemento debe ser entero"
            return listav2(lista)
        else:
            return "error en la entrada"
    else:
        return "debe ingresar una lista"       
def listav2(lista):
    num=[0]
    impar=[0]
    for elemento in lista:
        if elemento%2==0:
            num+=[1]
            continue
        if elemento%2!=0:
            impar+=[1]
            continue
        else:
            impar+=[3]
        if num[-1]==impar[-1]:
            continue
        else:
            return False
    return True
"""
nombre: matriz triangular inversa interior
entrada: matriz
salida true o false
restriccion minimo de fila y columna 4, multiplo de 3 
"""

def matriz_triangular_inversa(matriz):
    contador=largo(matriz[0])*-1
    m=largo(matriz)*-1
    validacion=validaMatriz*-1
    if validacion==True:
        final=m
        for elemento in matriz:
            elementos=[matriz[M]]
            while contador!=final:
                if elementos[contador]%3==0:
                    contador+=-1
                else:
                    return False
            M+=-1
            contador=largo(matriz[0])
        return True     
    
def largo(x):
    contador=0
    for elemento in x:
        contador+=1
    return contador
    


def validaMatriz(matriz):
    if isinstance(matriz,list):
        long1=largo(matriz)
        long2=largo(matriz[0])
        if long1==long2:
            if long1>=4:
                for elemento in matriz:
                    x=[elemento]
                    for caracter in x:
                        if isinstance (caracter,int):
                            continue
                        else:
                            return False
                    return True
                

"""
Nombre: multiplicacionMatrices
entrada: matriz1,matriz2
salida: multiplicacion
restriccion: que sea matriz
"""

def multiplicacionMatrices(matriz1,matriz2):
    columna=[]
    H=0
    c=0
    res=0
    long=largo(matriz1)
    rep=[]
    while x!=long:
        for x in matriz2:
            num=x[H]
            columna+=[num]
            for caracter in matriz1:


                num1=caracter[c]
                num2=columna[c]
                res=num1*num2
            rep+=[res]
            res=0
            c+=1
        columna=[]
        x+=1
    return volteador(rep)
def vermatriz(x):
    if isinstance(x,list):
        long1=largo(x)
        long2=largo(x[0])
        if long1==long2:
            for elemento in x:
                v=[elemento]
                for H in v:
                    if isinstance(H,int):
                        continue
                    else:
                        return False
            return True
        else:
            return False
    else:
        return False
def volteador (rep):
    list=[]
    H=0
    long=largo(matriz)#era rep
    c=0
    x=[]
    while H!=long:
        for caracter in rep:
            x+=[caracter[c]]
        list+=[x]
        x=[]
        c+=1
    return list


"""
nombre: sumasendiagonal
entrada:matriz
salida suma
restrccion:que sea cuadrado, impar
"""

def sumasEnDiagonal(matriz):
    if isinstance (matriz,list):
        long1=largo(matriz)
        long2=largo(matriz[0])
        if long==long2:
            if long1=long2:
                return sumasv2(matriz)
            else:
                return "debe ingresar tamaños impares"
        else:
            return "debe ingresar matriz cuadrada"
    else:
        return "debe ingresar una matrtiz"
    
def sumasv2(matriz):
    num=0
    cont=0
    cont2=largo(matriz[0])-1
    for elemento in matriz:
        x=elemento[cont]
        try:
            H=int(x)
        except:
            return "debe ingresar elementos int"
        num+=-1
        cont+=1
    for caracter in matriz:
        try:
            x=int(caracter[cont2])
        except:
            return "los caracter deben ser int"
        num+=x
        cont+=-1
    return num