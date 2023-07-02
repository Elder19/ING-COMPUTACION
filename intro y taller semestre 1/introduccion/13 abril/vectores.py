"""

Nombre suma de verctores
entrada: vectores
salida: suma
restriccion vectores mimso largo y entero
"""
def sumavertores(vector1,vector2):

    if isinstance(vector1,list):
         if isinstance(vector2,list):
             return sumav(vector1,vector2)

         else:
            return "Error el verctor 2 debe ser una lista"
    else:
        return"Error el verctor 2 debe ser una lista"
def sumav(vector1,vector2):
    indice=0
    resultado=[]
    t1=largo(vector1)
    t2=largo(vector2)
    l=t1
    while indice<l:
        if t1==t2:
            if isinstance(vector1[indice],int) and  isinstance(vector2[indice],int):
                resultado+=vector1[indice]+vector2[indice]
                indice+=1
        else:
            resultado="Error: Los valores de los vectores deben ser enteros"
            break
    return resultado



def largo(x):
    contador=0
    for i in x:
        contador+=1
    return contador

#print(sumavertores([1,2],[2.2]))




"""

Nombre resta de verctores
entrada: vectores
salida: resta
restriccion vectores mimso largo y entero
"""
def sumavertores(vector1,vector2):

    if isinstance(vector1,list):
         if isinstance(vector2,list):
             return sumav(vector1,vector2)

         else:
            return "Error el verctor 2 debe ser una lista"
    else:
        return"Error el verctor 2 debe ser una lista"
def sumav(vector1,vector2):
    indice=0
    resultado=[]
    t1=largo(vector1)
    t2=largo(vector2)
    l=t1
    while indice<l:
        if t1==t2:
            if isinstance(vector1[indice],int) and  isinstance(vector2[indice],int):
                resultado+=vector1[indice]-vector2[indice]
                indice+=1
        else:
            resultado="Error: Los valores de los vectores deben ser enteros"
            break
    return resultado

"""
Nombre: escalar
entrada: vector
salida: producto elevad al escalar
restricciones

"""
def escalares(vector1,escalar):
    y=escalar

    if isinstance(vector1,list):
        if isinstance(escalar,int):
            return escalaraux(vector1,y)
        else:
            return "El escalar debe ser entero"
    else:
        return "Error el verctor 2 debe ser una lista"
    

def escalaraux(x,y):
    resultado=[]


    for i in x:
        if isinstance(i,int):
     
            resultado+=[i*y]
        else:
            return"Error el elmento de la lista de la lista no es entero"
    return resultado

print(escalares([1,2],3))


"""

Nombre resta de verctores
entrada: vectores
salida: resta
restriccion vectores mimso largo y entero
"""
def productoescalar(vector1,vector2):

    if isinstance(vector1,list):
         if isinstance(vector2,list):
             return escalar_aux(vector1,vector2)

         else:
            return "Error el verctor 2 debe ser una lista"
    else:
        return"Error el verctor 2 debe ser una lista"
def escalar_aux(vector1,vector2):
    indice=0
    resultado=0
    t1=largo(vector1)
    t2=largo(vector2)
    l=t1
    while indice<l:
        if t1==t2:
            if isinstance(vector1[indice],int) and  isinstance(vector2[indice],int):
                resultado+=(vector1[indice]*vector2[indice])
                indice+=1
        else:
            resultado="Error: Los valores de los vectores deben ser enteros"
            break
    return resultado
#print(productoescalar([2,5,8],[3,6,9]))