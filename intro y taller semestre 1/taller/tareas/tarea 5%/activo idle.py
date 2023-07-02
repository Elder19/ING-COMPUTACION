def Registraractividad():
    contenido=()
    codigo="f"
    txt=input("Digite la fecha de hoy")
    txt1=input(" Digite la hora actual")
    txt2=input("Digite su nombre du usuario")
    txt3= input("Digite la aplicacion correspespondiente")
    txt4 =input("Digite su mensaje")
    #try:
        #txt=str(txt)
       # txt1=str(txt1)
        #txt2=str(txt2)
        #txt3= str(txt3)
        ##txt4=str(txt4)
    #except:
        #return"El parametro no se puede convertir en texto"
    print ("Se esta ejecuntado el registro de la actividad")
    contenido=(codigo,txt,txt1,txt2,txt3,txt4)
    print(contenido)
    name=nombre()
    #print (name)


    
    print ("Se esta ejecuntado el registro de la actividad")
    return escribirArchivo(name, contenido, "a")


    
def escribirArchivo(nombreArchivo, contenido, mode):
    print(nombreArchivo)
    if (isinstance(nombreArchivo, str) and (contenido, str)):
        if (nombreArchivo!=""):
            archivo=open (nombreArchivo,mode )
            try:
                contenido=str(contenido)
            except:
                return "Error al incorporar su mensaje"
            archivo.write (contenido)
            #print( contenido)
            archivo.close()
            return contenido
          
        else:
            return "Error: nombre no debe ser vacio"
       
    else:
        return "error, paramentro no es texto"
def nombre():
    nombreAr="bitacora2.txt"
    return nombreAr
#print(nombreAr)
        
"""

Nombre: buscarEnTexto
Entrada: texto, valorBuscar 
Salida: Expone las lineas donde hay conicidencia
Restricciones:
    El texto y el valor deben ser string
"""
def Buscarporusuario():
    if isinstance(valorBuscar, str):
         if valorBuscar in texto:
                
         else:
             
             
