"""
nombre3: xonvertir numeros
entrada num potencia
salida nuevo numero
restricciones: potencia y num != vacio
"""
def convertirNumero(num, exponente):
    if isinstance(num, int) and isinstance(exponente, int):
        return convertirNumeroAux(num, exponente)
       
    else:
        return 'Error: Debe ser entero'
def convertirNumeroAux(num,potencia):
    ladoD=num
    ladoI=num
    contador=0
    largo=num
    centro=[]
    numero=0
    cut=contador
    derecha=None
    izquierda=None
    centro=None
    
    while largo!=0:
        largo=largo//10
        contador +=1
    if contador%2!=0:

        #sacar lado derecho
        divisor=10**(contador//2+1)
        derecha=ladoD//divisor
        divisor1=10**(contador//2)
        izquierda=ladoI%(divisor1)
        
        #sacar centro
        divisor=10**(contador//2)
        cent=ladoD//divisor
        centro=cent%10
        centro=centro**potencia
        x=par_impar(derecha,izquierda,centro)
       
def par_impar(derecha,izquierda,centro):
    contadorpar=1
    NIMPAR=0
    contadorimpar=1
    respuestaimpar=0
    respuestapar=0
    while derecha!=0:
        num=derecha%10
        if num%2==0:
            respuestapar=(respuestapar**contadorpar)+num
            contadorpar+=1
           
        derecha= derecha//10

    while izquierda!=0:
        if izquierda>0:
            num=izquierda%10
            if num%2!=0:
                respuestaimpar=(respuestaimpar**contadorimpar)+num
                contadorimpar+=1
            izquierda=izquierda//10
            #print("g")
        else:
            NIMPAR=1
    return unirnum(respuestapar,respuestaimpar,centro,NIMPAR)
    
       
def unirnum(dere,izq,cent,impar=None):
    #print("v")
    respuesta=izq
    largor=largon(respuesta)
    respuesta=(respuesta**largor)+cent
    largor=largon(respuesta)
    respuesta=(respuesta**largor)+dere
    #print(respuesta)
    if impar==1:
        respuesta*=-1
        return respuesta
    return respuesta
    

        

            
def largon(n):
    n1=[n]
    contador=0
    for caracter in n1:
        contador+=1
    return contador
            

"""
nombre: invertir lista
entrada:lista
salida nueva lista
restrcciones: debe ser slista
"""

def invertirLista(lista):
    if isinstance(lista,list):
        return invertirLista_Aux(lista)
    else:
        return "el parametro debe ser una lista"
    
def invertirLista_Aux(lista):
    llargo=largon(lista)
    if llargo>2:
        Nlista=[]
        for elemento in lista:
            if isinstance (elemento,int):
                Nlista=[elemento]+Nlista
            else:
                return"Error: La lista debe elementos tipo entero"
        return Nlista
            
    else:
        return "Error: La lista debe contener al menos 2 elementos"
    
def extremosLista(lista):
    if isinstance(lista, list):
        return extremosLista_Aux(lista)
    else:
        return "Parametro debe ser una lista"      
    
def extremosLista_Aux(lista)(lista):
    numeroMenor = lista[0]
    for elemento1 in lista:
        minimo=elemento1
        #print(minimo)
        for elemento in lista:
            #print("s")
    for digito in lista: #menor
        if isinstance(digito, int):
            if numeroMenor  > digito:
                numeroMenor = digito
        else:
            return "Digito debe ser un número entero"
                #print (minimoN)
            else:
                continue
    for elemento in lista:
         maxN=elemento
         for elemento in lista:
            if elemento>minimo:
                maxN=elemento
                #print (maxN)
            else:
                continue 
    return[numeroMenor,maxN]
