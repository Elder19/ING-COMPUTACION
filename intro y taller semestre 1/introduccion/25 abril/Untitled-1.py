def chekearmatriz(matriz):
     if isinstance (matriz,list):
          if matriz!=[]: #varifica las columnas
               largos=largo(matriz[0])
               for lista in matriz:
                    listas=largo(lista)
                    if listas==largos:
                         continue
                    else:
                         return "Error la matriz no cumple con los rangos"
               largomatriz=largo(matriz)
               if largomatriz==largos:
                    return True
               else:
                    return False 
               
def largo(x):
    contador=0
    if (x,list):
   
        for elemento in x:
            contador+=1
        return contador
                

def diagonalmatriz(matriz):
     tf=chekearmatriz(matriz)
     if tf==True:
        suma=[]
        contador=0
        for elemento in matriz:
            suma+=[elemento[contador]]
            contador+=1
        return suma
     else:
          return ("La matriz no cumple con los rangos indicados")

def esMatrizTriangularSuperior(matriz):
    tf=chekearmatriz(matriz)
    if tf==True:
        contador=1
        largo=0
        comparador=[]
        for elemento in matriz:
            while contador<=largo:
                comparador+= elemento[0:contador]
                comparadors=elemento[contador:]
                for elemento in comparadors:
                        if elemento!=0:
                            continue
                        else:
                            return False
                contador+=1
            largo+=1
        
        for elemento in comparador:
            if elemento ==0:
                continue
            else:
                return False
        return True 
    else:
          return ("La matriz no cumple con los rangos indicados")


                
     



#print(diagonalmatriz([[2,4,99],[90,1,67],[75,91,37]]))
print(esMatrizTriangularSuperior([[2,5,1,9],[0,2,3,1],[0,0,9,1],[0,0,0,9]]))