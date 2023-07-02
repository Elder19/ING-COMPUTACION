
def verificarmatriz(matriz):
    if isinstance(matriz,list):
        long=largo(matriz)
        long2=largo (matriz[0])
        if long==long2:
            return numerosiguales(matriz,0,long)
        else:
            return False       
    else:
        return "Error debe ingresar una lista " 
def numerosiguales(lista,contador,long): 
    if contador==long-1:
        return True
    else:
        veri= vector(lista[contador])
        if veri==True:
            long3=largo(lista[contador])
            if long==long3:
                return numerosiguales(lista,contador+1,long) 
            else:
                return False
        else:
            return False
def vector(lista):
    if lista==[]:
        return True
    else:
        if isinstance(lista[0],int):
          
            
            return vector(lista[1:])
        else:
            return False   
def largo(x):
    if x==[]:
        return 0
    else:
        x=x[1:]
        return largo(x)+1
    


def girar(matriz):
    x=verificarmatriz(matriz)
    if x==True:
        return girar2(matriz,-1)
    else:
        return "Error su matriz no cumple con los parametros"
    
    
def girar2(matriz,contador):
    long=largo(matriz)
    if long<contador*-1:
            return [[]]
    else:
         return [matriz[contador]]+girar2(matriz,contador+-1)
        

    
    
    
    
    
"""
nombre: formarMatriz
entrada (filas, columnas)
salida matriz
restriccion: que los parametros sean enteros
"""
def formarMatriz(filas, columnas):
    if not(filas,int):
        return "Las filas deben ser de caracter entero"

    if not(columnas,int):
         return "Las columnas deben ser de caracter entero"
    return matriz2(filas, columnas,0,[])

def matriz2(filas,columnas,contador,matriz):

    if contador==filas:
        return matriz3(filas, columnas,0,matriz,0,0)
    else:
        matriz+=[[]]
        return matriz2(filas, columnas,contador+1,matriz)
    
    

def matriz3(filas, columnas,contador,matriz,indice,numeros):
    if contador==columnas:
        return matriz
    else:
        
        matriz=integran(matriz,indice,0,numeros)
        long=largo(matriz)
        return matriz3(filas, columnas,contador+1,matriz,indice+1,numeros+long)

def integran(matriz,indice,contador,numeros):
    long=largo(matriz)
    if contador==long:
        return matriz
    else:
        matriz[indice]+=[numeros]
       
        return integran(matriz,indice,contador+1,numeros+1)





print(formarMatriz(5,5))
    
    