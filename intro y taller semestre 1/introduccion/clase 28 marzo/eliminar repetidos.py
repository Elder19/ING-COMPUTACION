"""
nombre:eliminarduplicados
entrada:lista
salida: lista sin repetidos
restriccion
"""
def eliminarelemento (lista):
    res=[]
    largo=largon(lista)
    contador=lista
 
    while contador>0:
        
        num=lista[contador]
        #print (num)
        caracter=largon([num])
        rep=largo(lista,num)
        
        if rep>caracter:
            res+=[num]
         
          
            
        if rep==caracter:
            res+=[num]
        contador-=1    
        lista=lista[1:]
    return res
            
            
            
def largon(n):
    l=0
    for caracter in n:
        l+=1
    return l  
def largo(lista,num):
    
    rep=0

    for caracter in lista:
        if caracter==num:
            rep+=1
        else:
            continue
    return rep
