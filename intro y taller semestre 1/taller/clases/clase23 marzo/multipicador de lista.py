"""Nombre:multi
entrada:lista
salida:multiplicacion
restriccion no debe ser nula
"""
def multi(lista):
    numero=0
    respuesta=1
    if lista!=[]:


        for elemento in lista:
            numero=elemento
            print("x")
            respuesta=respuesta*numero
        return respuesta  
    else:
        return "la lista no debe ser nula" 
print (multi([1,2,5]))

def multiw(lista):

    numero=0
    respuesta=0
    if isinstance(lista!=[]):
        while lista!=[]:
            respuesta=1
            numero=[0]
    
            respuesta*=numero
            lista[1:]
        
            
                
    else:
        return "la lista no debe ser nula"   


def contarparesImpares(lista):
    contadorI=0
    contadorP=0
    respuesta1=0
    respuesta2=0
    respuesta3=[]

    for elemento in lista:
        if isinstance (elemento,bool):
            continue

        if elemento%2==0:
            contadorP+=1
        else:
            contadorI+=1
              
        respuesta1+=1
        respuesta2+=1
        respuesta3=[respuesta1,respuesta2]
       
    return respuesta1, respuesta2 

def contarparesImparesw(lista):


    while lista!="":
        num=[0]
        respuesta=[]
        contadorI=0
        contadorP=0
        if isinstance (lista,bool):
            continue 
        if num%2==0:
            contadorP+=1
        else:
            contadorI+=1
        lista[1:] 
        respuesta[contadorI,contadorP]
       
           
    return respuesta     
        
print(contarparesImparesw([1,2,3,4]))

