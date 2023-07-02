"""
nombre:separarParesImpares
entrada:lista
salida: listas de pares e impares
restrciiones
"""
def separarParesImpares(lista):
    
    par=[]
    impar=[]
   
    if isinstance (lista,list):
     
        for elemento in lista:
            if elemento%2==0:
                par+=[elemento]
               
            else:
                impar+=[elemento]
              
                
        return [par,impar]

    else:
        return "Lista no puede ser vacio"

