def convertirBase():
    print("--------------------------------------------")
    print("Menu de opciones")
    print("--------------------------------------------")

    print( "decimal a base 2 (2)")
    print( "decimal a base 3 (3)")
    print( "decimal a base 4 (4)")
    print( "decimal a base 16 (5)")
    print( "base 16 a base 10 (6)")
    print( "base 2 a  decimal (7)")
    print( "base 3 a  decimal (8)")
    print( "base 4 a  decimal (9)")

    opcion=input("Ingrese una de las opciones")
    try:
        opcion=str(opcion)
    except:
    
            print("Debe digitar una de las opciones vaidas")
            return  calculadora()



    if opcion!="":
        if opcion=="2":
            variable=int(input("Ingrese el numero que desea convertir"))
            return base10abase2(variable)


        if opcion=="3":
            variable=int(input("Ingrese el numero que desea convertir"))
            return base10abasex(3,variable)

 
        if opcion=="4":
            variable=int(input("Ingrese el numero que desea convertir"))
            return base10abasex(4,variable)
        
        if opcion=="5":
            variable=int(input("Ingrese el numero que desea convertir"))
            return decimalhexa(variable)
        
        if opcion=="6":
            variable=input("Ingrese el numero que desea convertir")
            return  hexaadecimal(variable)
        if opcion=="7":
            variable=int(input("Ingrese el numero que desea convertir"))
            return binarioa10(variable)
        if opcion=="8":
            variable=int(input("Ingrese el numero que desea convertir"))
            return basexa10(3,variable)
        if opcion=="9":
            variable=int(input("Ingrese el numero que desea convertir"))
            return basexa10(4,variable)
       
"""
Nombre: hexaadecimal
entrada  h
salida conversion a base 10
restricciones:
"""         
        
def hexaadecimal(h):
    contador=0
    decimal=0

    h=str(h)
    for elemento in h:
        
        residuo=elemento

        if residuo=="A":
            red=10
        elif residuo=="B":
            red=11
        elif residuo=="C":
            red=12
        elif residuo=="D":
            red=13
        elif residuo=="E":
            red=14
        elif residuo=="F":
            red=15

       
            
        elif residuo=="1":
                red=1
        elif residuo=="2":
                red=2
        elif residuo=="3":
                red=3
        elif residuo=="4":
                red=4
        elif residuo=="5":
                red=5
        elif residuo=="6":
                red=6
        elif residuo=="7":
                red=7
        elif residuo=="8":
                red=8
        elif residuo=="9":
                red=9
                      
                
                
                
                
                
                    
        decimal=decimal*16+red
        #decimal+=red*(2**contador)
        contador+=1
           
    return( decimal)
 

#print( hexaadecimal("1B58"))


"""
Nombre: binarioa10
entrada  binario
salida conversion a base 10
restricciones:
""" 

def binarioa10(binario):
    numero=0
    contador=0
    while binario!=0:
        num=binario%10
        trans=num*2**contador
        numero+=trans
        contador+=1
        binario=binario//10
 
    return( numero)
    """
    opcion=input("(1) salir, (2) menu principal")
    if opcion=="1":
        return "Gracias"
    if opcion=="2":
        return calculadora()
    else:
        return calculadora()
    """
"""
Nombre: base10abase2
entrada  base
salida conversion a base 2
restricciones:
""" 
def base10abase2(base):
    contador=0
    bi=0
    while base!=0:
       
       
        residuo=base%2
        base=base//2
        bi=bi+(residuo*(10**contador))
        contador+=1
    return bi
    
"""
Nombre: base10abasex
entrada f,base
salida conversion a base que el usuario quiere
restricciones:
""" 





def base10abasex(f,base):
    contador=0
    bi=0
    while base!=0:
       
       
        residuo=base%f
        base=base//f
        bi=bi+(residuo*(10**contador))
        contador+=1
   

    return bi
"""
Nombre: basexa10
entrada f,base
salida conversion a base 10
restricciones:
"""    

def basexa10(f,base):
    contador=0
    bi=0
    while base!=0:
       
        
        residuo=base%10
        bi=bi+(residuo*(f**contador))
        contador+=1
        base=base//10
    return bi
    
"""
Nombre: decimalhexa
entrada numero
salida conversion a hexadecimal
restricciones:
"""
def decimalhexa(numero):
    respuesta=""

    while numero>0:

        residuo=numero%16
        
        if residuo==10:
            respuesta="A"+respuesta
        elif residuo==11:
            respuesta="B"+respuesta
        elif residuo==12:
            respuesta="C"+respuesta
        elif residuo==13:
            respuesta="D"+respuesta    
        elif residuo==14:
            respuesta="E"+respuesta
        elif residuo==15:
            respuesta="F"+respuesta  
        else: 
            residuo=str(residuo)
            respuesta=residuo+respuesta
        numero=numero//16

    return respuesta
  
#print(decimalhexa(1100))   
           
def largo(X):

    contador=0
    for i in X:
        contador+=1
    return contador


