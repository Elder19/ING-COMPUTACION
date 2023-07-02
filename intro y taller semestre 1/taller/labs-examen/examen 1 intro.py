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
                print(resultado)
            divisor+=1
        if resultado>(num*2):
            return True
        else:
            return False
    else:
        return "el numero debe ser entero mayor a 0"
"""
nombre:adyacentesimpares
entrada:num
salida: true o false
restricciones
"""
def adyacentesimpar(num):
    digito1=0
    digito2=0

    if isinstance (num,int):
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
        return "numero debe ser entero"

"""
nombre: formanumero
entrada:lista
salida: nuevonumero
restricciones: debe ser lista, si hay negativos respuesta negativa
"""
def formarNumero(lista):
    resultado=0
    if isinstance (lista,list):
        for elemento in lista:
            resultado=resultado*10
            resultado=resultado+elemento
            if elemento<0:
                resultado*=-1

        return resultado
    else:
        return "el parametro debe ser una lista"

"""
nombre: valorsecuencia
entrada:num grupo llave
salida: true o false
restricciones: debe ser entero y posotivos
"""
def validarSecuencia (num,grupo,llave):#validacion
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
        contador+=1
    
    return modulo
def validarSecuencia2(num,grupo,llave):
    modulo=10
    digito=0
    resultado=0
    moduloT=modulo%10
    numero=0
    if grupo>0:
            modulo=crearmodulo(grupo)#esta bajo validacion
            while num>0:
        
                digito=num%modulo
                #num=num//modulo
                resultado+=digito
                print(resultado)
                num=num//modulo
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
    while contador <num:
        if num % contador == 0:
            total+=primos(contador)
            print(total)
        contador+=1
    if total >=2:
        return True
    else:
        return False
  
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
def numeropolimax():
    if isinstance (num,int):
        return numeropolimax2(num)
    else:
        return "num debe ser entero"



def numeropolimax2( num):
    contadorimpar2=0
    contadorpar2=0
    dv=largo(num)
    mod=dv/2
    premodulo=crearmodulo2(mod)
    while num>0:
        print(premodulo)
        digito1=num%premodulo
        num=num//premodulo
        digito2=num%premodulo
        if  digito1%2==0:
            contadorpar2+=1

        else:
            contadorimpar2+=1
        if  digito2%2==0:
            contadorpar2+=1

        else:
            contadorimpar2+=1    
    if contadorpar2==contadorimpar2:
        return True
    else:
        return False    


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
    contador=1
    if num==1:
        return modulo
    while contador<=num:
        modulo*=10
        contador+=1
  
