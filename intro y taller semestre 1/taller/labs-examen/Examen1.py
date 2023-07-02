"""
nombre:numeroAbundante
entrada:num
salida:true o false
restricciones: debe ser entero positivo
"""
def numeroAbundante(num):
    digito=0
    divisor=1
    resultado=0
    if isinstance (num,int) and num>0:
        while divisor<=num:
            digito=num
            if digito % divisor==0:
                resultado+=divisor
                #print(resultado)
            divisor+=1
        if resultado>(num*2):
            return True
        else:
            return False
    else:
        return "Error en la entrada, debe ser número positivo"
"""
nombre:adyacentesimpares
entrada:num
salida: true o false
restricciones
"""
def  adyacentesImpares(num):
    digito1=0
    digito2=0

    if num>0:
        while num>0:
            digito1=num%10
            num=num//10
            digito2=num%10
            num=num//10
            if (digito1+digito2)%2!=0:
                continue
            else:
                return False
        return True
    else:
        return "Número no se puede procesar"

"""
nombre: formanumero
entrada:lista
salida: nuevonumero
restricciones: debe ser lista, si hay negativos respuesta negativa
"""
def  formarNumero(lista):
    resultado=0
    contador=0
    if isinstance (lista,list):
        for elemento in lista:
            if elemento<0:
                elemento*=-1
                contador=1
            if elemento == 0:
                resultado=resultado*10+elemento
            if elemento!=0:
                potencia=largon(elemento)
                resultado=resultado*(10**potencia)+elemento

        if contador == 1:
            resultado *=-1
    
        
        return resultado
    else:
        return "el parametro debe ser una lista"
def largon(num):
    contador=0
    if num==0:
        contador+=1
    else:
        while num!=0:
            contador+=1
            num//=10
    return contador


"""
nombre: valorsecuencia
entrada:num grupo llave
salida: true o false
restricciones: debe ser entero y posotivos
"""
def  validarSecuencia (num,grupo,llave):#validacion
    if isinstance (num,int):
        if isinstance (grupo,int):
            if isinstance (llave,int):
                return validarSecuencia2(num,grupo,llave)
            else:
                return "llave debe ser entero"
        else:
            return"grupo debe ser entero"
    else:
        return"num debe ser entero"

def crearmodulo(grupo):
    modulo=10
    contador=1
    if grupo==1:
        return modulo
    while contador<=grupo:
        modulo*=10
        contador+=2
    
    return modulo
def validarSecuencia2(num,grupo,llave):
    modulo=10
    digito=0
    resultado=0
    numero=0
    if grupo>0:
            modulo=crearmodulo(grupo)#esta bajo validacion
            #print(modulo)
            while num>0:
        
                digito=num%modulo
                r=digito//10**(grupo-1)
                resultado+=r
                #print(resultado)
                num=num//modulo
                #print(num)
            if resultado==llave:
                return True
            else:
                return False           
"""
nombre: numero hermano
entrada:num
salida true o false
restricciones uno es primo
"""
def numeroHermano(num):
    if isinstance (num,int):
        return  numeroHermano_aux(num)
    else:
        return "num debe ser entero"
def numeroHermano_aux(num):
    contador=2
    total=0
    if num>0:
        while contador <num:
            if num % contador == 0:
                total+=primos(contador)
                #print(total)
            contador+=1
        if total >=2:
            return True
        else:
            return False
    else:
        return "Error: Número debe ser positivo"
def primos(numero):
    divisor = 2
    resultado = 0
    total=1

    if numero > 0:
    
        while divisor < numero and resultado ==0:
            total = numero % divisor 
            if total ==0:
                resultado +=1
            divisor+=1
        if resultado == 0:
            total=1
            return total
        else:
            return total

"""
nombre:numeropolimax
entrada:num
salida:true o false}
restrcciones:debe ser largo par
"""
def  numeroPolimax(num):
    largonN=largo(num)
    contadorpar=0
    contadorimpar=0
    if num<0:
        num*-1
    if num<10:
        return False 
        
  

    if largonN % 2==0:
        while num>0:
          dividendo=num%10
          if dividendo%2==0:
              contadorpar+=1
          else:
              contadorimpar+=1
          num=num//10
        if contadorimpar%2==0:
          return True
        else:
         return False 
      
  
    else:
        return "Error el numero debe tener una cantidad de digitos par"

   

def largo(num):

    numero=0
    contador=0
    while num>0:
        numero=num%10
        
        contador+=1
        num=num//10
        

    return contador
    
def crearmodulo2(num):
    modulo=10
    contador=0
    if num==1:
        return modulo
    contador//2
    while contador!=num:
        modulo*=10
        contador+=1




