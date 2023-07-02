"""
Nombre:cheak_matriz
Entrada: matriz
"""
def cheak_matriz(matriz):
        
        cantidadm=0
                   
        contador=0
        posicion=0
        lista=[]
        if isinstance (matriz,list):#verifica el largo de las matriz que sean iguales
            x=(matriz[0])
            x= largotxt(x)
            longmatriz=str(largotxt(matriz[0]))
            for elemento in matriz:
                print(elemento)
                x=largotxt(elemento)
                x=str(x)
                if x==longmatriz:
                    continue
                else:
                    return "Error la matriz no cumple con el largo correcto"
            """
            for s in matriz:
                cantidadm+=1
                largo=largotxt(s)#valida largo de columna
                if largo==x:
                    continue
                else:
                      return "Error la columna en la matriz no cumple con el largo correcto"
            """
            for x in matriz:
                if x[0][0]==float:
                    if x>-1:
                    
                            return comparador(1,matriz) 
                    else:
                          return"Error contiene datos hetereogeneos"
                    
                elif elemento[0][0]==int:
                     if elemento>-1:
                    
                            return comparador(2,matriz)     
                     else:
                          return"Error contiene datos hetereogeneos"

def largotxt(x):
    if (x,list):
       
        contador=0
        for elemento in x:
            contador+=1
        return contador
    else:
          return contador
                      
def comparador(num,vector):
     contador=0
     posicion=0
     lista=[]
     if num==1:
         dif=(lista,float)
     elif num==2:
         dif=(lista,int)

     
     lista=vector[contador][posicion]

     largo=largotxt(lista)

     if lista[contador][posicion]:
         if isinstance (dif):
             posicion+=1
             if posicion ==largo:
                 contador +=1
                 posicion=0

def sumarfuncion(matriz1,matriz2):
     contador=0
     x=0
     listafinal=[]
     nuevalista=[]
     largo=largotxt(matriz1[0])
     for elemento in matriz1:
        while contador<largo:
            num1=matriz1[x][contador]
            num2= matriz2[x][contador]
            nuevalista+=[num1+num2]
            contador+=1
        x+=1
        contador=0
        listafinal+=[nuevalista]
        nuevalista=[]
     return listafinal

def multiplicarmatriz(matriz1,matriz2):
     respuesta=0
     columnas=[]
     c=0
     largo=largotxt(matriz2)
     x=0
     rep=[]
     r=0
     z=[]
     final=[]
     lista=0
     posicion=0
     while x<largo:
        for elemento in matriz2:
               num=elemento[x]
               columnas+=[num]
        for elemento in matriz1:
                largom=largotxt(matriz1[0])
                while c<largo:
                          
                     num1=elemento[c]
                     num2=columnas[c]
                     respuesta=num1*num2
                     r+=respuesta
                     c+=1
                     
                c=0
                rep=rep+[r]
                r=0
                respuesta=0
        z+=[rep]
        rep=[]    
        x+=1
        columnas=[]
     
     stop=largo*largom
     while stop>0 :
          
          
            rep+=[z[lista][posicion]]
            
            lista+=1
            stop-=1
                
            if lista==largo:
                 
                 posicion+=1
                 lista=0
                 final+=[rep]
                 rep=[]
                
            
            continue
           
     return final
        

def sumarmatrizdiagonal(matriz):
     suma=0
     contador=0
     for elemento in matriz:
          suma+=elemento[contador]
          contador+=1
     return suma
"""        
def multiplicarMatriz(matriz1, matriz2):
    fila1 = contarFilas(matriz1)
    columna1 = contarColumnas(matriz1)
    fila2 = contarFilas(matriz2)
    columna2 = contarColumnas(matriz2)
    if columna1 == fila2 :
        indiceComun = 0
        indiceFila = 0
        indiceColumna = 0
        matriz = []
        while indiceFila < fila1 :
            vector = []
            while indiceColumna < columna2 :
                suma = 0
                while indiceComun < columna1 :
                    multiplicacion =matriz1[indiceFila][indiceComun] * matriz2[indiceComun][indiceColumna]
                    suma += multiplicacion
                    indiceComun += 1
                vector += [suma]
                indiceColumna += 1
                indiceComun = 0
            indiceFila += 1
            indiceColumna = 0
            matriz += [vector]
        return matriz
def contarColumnas(matriz):
    contador = 0
    vector = matriz[0]
    for numero in vector:
        contador += 1
    return contador

def contarFilas(matriz):
    contador = 0
    for fila in matriz:
        contador += 1
    return contador
    
    """
print(multiplicarmatriz([[1,0],[0,2]],[[5,7,],[1,3]]))