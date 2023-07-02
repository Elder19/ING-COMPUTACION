def vector(vector):
    contador=0
    posicion=0
    lista=[]
    if isinstance(vector,list):

        lista=vector[contador][posicion]

        for elemento in lista:
            if (elemento,str):
                return comparador(1,vector)
            elif (elemento,int):
                return comparador(2,vector)
def comparador(num,vector):
     contador=0
     posicion=0
     lista=[]
     if num==1:
         dif=(lista,str)
     elif num==2:
         dif=(lista,int)

     
     lista=vector[contador][posicion]

     largo=largol(lista)

     if lista[contador][posicion]:
         if isinstance (dif):
             posicion+=1
             if posicion ==largo:
                 contador +=1
                 posicion=0

         else:
             return "El vector no cumple con los requisitos"
             
         

def largol(lista):
    contador=0
    for elemento in lista:
        contador+=1
    return contador 

def encontrarMayor(vector):
    n=0
    contador=0
    long=largol(vector)
    if long>1:
        for x in vector:
            lista=vector[contador]


            for h in lista:
                contador+=1
                if n>h:
                    continue
            
                else:
                    n=h
        return n
        
def eliminarRepetidos(vector):
      delete=[]
      contador=0
      for x in vector:
            lista+=vector[contador]
      for elemento in lista:
          nm=elemento
          for x in lista:
              if nm == lista[contador]:
                  
                  delete+=[nm]
                  contador+=1
              else:
                  contador+=1
                  continue
      for x in delete:

           for elemento in lista:      
              
        
              
              
          
       


    
      
    

