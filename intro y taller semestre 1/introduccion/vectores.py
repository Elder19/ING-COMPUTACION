def creamatriz(fila,columna):
    contador=fila
    stop=columna
    cont=0
    numeros=0
    nlista=[]
    h=0
    vector=[]
    while h!=contador:
       
        while cont<=stop:
            nlista+=[numeros]
            numeros+=1
            cont+=1
            if stop==cont:
                h+=1
                vector+=[nlista]#que se haga losta
                
                cont=0
    return vector
#print(creamatriz(3,3))
def SumarFilasMatriz(matriz):
    contador=0
    n=0
    x=n
    cantidad=0
    posicion=0
    linea=0
    nmatriz=[]
    for elemento in matriz:
        cantidad+=1
        largo=[elemento]
        for elemento in largo:
            contador+=1
            n=contador
        if contador==x:
            if (elemento,str):
                dif=(elemento,str)
            elif(elemento,int):
                dif=(elemento,int)
            else:
                return ("Lo indicado no es una matriz")
            
    while cantidad!=0:

        
        nmatriz+=[matriz[0][posicion]+matriz[linea][posicion]]
        posicion+=1
        linea+=1
        cantidad+=-1
        if posicion==contador:
            posicion=0

    return nmatriz

