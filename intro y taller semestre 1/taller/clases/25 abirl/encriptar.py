

def encriptar(name):
    encript=""
    h=1
    contenido=leerArchivoread(name)
    if contenido!="":
        for elemento in contenido:
            num=ord(elemento)
            dc=decimalhexa(num)
    
            long=largot(dc)
            if long<3:
                dc="0"+dc

            encript+=dc
            
            #if h==1:
                #encript="0"+encript
                #h=0
        nombret="encriptar.txt"
        
        escribirArchivoa(encript,nombret)
    return "Se encripto su mensaje"
    
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

"""
    Nombre: Escribir archivo a
    Funcion:escribe palabra por palabra en el texto
    Restricciones: el nombre del archivo debe ser str,el contenido ni el nombre puede estar vacio
    """
def escribirArchivoa(elemento,nombre):
  
    nombreArchivo=nombre
    
    if (isinstance(nombreArchivo,str)):
        if (nombreArchivo!=""):
            
                archivo=open (nombreArchivo,mode="w" )
                archivo.write(elemento)
                archivo.close()
                
        else:
            return "debe ingresar el nombre de el documento"
def leerArchivoread(nombreArchivo):
    #validar nombreArchivo debe ser string
    if (isinstance(nombreArchivo,str)):
        if (nombreArchivo != ""):
            archivo =open(nombreArchivo, mode= "r")
            contenido = archivo.read()
            archivo.close()
            return contenido
        else:
            return "ERROR EL ARRCHIVO NO DEBE SER VACIO"
    else:
        return" tipo no es texto"
def largot(X):
    contador=0
    for c in X:
        contador+=1

    return contador
