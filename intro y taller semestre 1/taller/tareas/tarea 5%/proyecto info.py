"""
trabajo de programacion
"""
def RegistrodeBitácoras():
    print("==================================")
    print("")
    print("              bitacora           ")
    print("")
    print("==================================")
    print(" opciones")
    print("")
    print("     1:Registro de Actividades ")
    print("")
    print("     2:Búsquedas")
    print("")
    print("     3:Cantidad de mensajes ")
    print("")
    print("     4:Guardar mensajes ")
    print("")
    print("     9:Salir ")
    print("")
    print("==================================")
    print("")


    opcion = input("Digitar una opcion: ")

    if opcion != "":
        try:
            opcion = int(opcion)
        except:
            return "Error: el valor de la opcion debe ser numerico "
        else :  #el else se ejecuta cuando no genero el try
            if opcion == 1:
                return Registrodeactividades()
            elif opcion == 2 :
                return Búsquedas()
            #elif opcion == 3 :
                #return Cantidaddemensajes()
           # elif opcion == 4 :
               # return Guardarmensajes()
            elif opcion == 9:
                return salir()
            else :
                return"Error: opcion no reconocido"

def salir():
    print("")

    print("==================================")
    print("            Gracias")
    print("==================================")
def Registrodeactividades():
    print("===========================================")
    print("    opciones de Registro de Actividades ")
    print("===========================================")
    print("     opciones")
    print("")
    print("     1:Registrar actividad")
    print("")
    print("     2:Borrar actividad")
    print("")
    print("     3:Modificar actividad")
    print("")
    print("     4:Ver todas las actividades")
    print("")
    print("     5:retorna")
    print("")
    print("===========================================")
    print("")
    opcion = input("Digitar una opcion: ")

    if opcion != "":
        try:
            opcion = int(opcion)
        except:
            return "Error: el valor de la opcion debe ser numerico "
        else :  #el else se ejecuta cuando no genero el try
            if opcion == 1:
                return Registraractividad()
            elif opcion == 2 :
               return Borraractividad()
            elif opcion == 3 :
                return Modificaractividad()
            #elif opcion == 4 :
               # return Vertodaslasactividades()
            elif opcion == 5 :
               return Retornar()
            else :
                return"Error: opcion no reconocido"
def Búsquedas():
    print("===========================================")
    print("    opciones de Búsquedas  ")
    print("===========================================")
    print("     opciones")
    print("")
    print("     1:Buscar por usuario")
    print("")
    print("     2:Buscar por aplicación")
    print("")
    print("     3:Buscar por fecha ")
    print("")
    print("     4:Retornar ")
    print("")
    print("===========================================")
    print("")
    opcion = input("Digitar una opcion: ")

    if opcion != "":
        try:
            opcion = int(opcion)
        except:
            return "Error: el valor de la opcion debe ser numerico "
        else : # else se ejecuta cuando no genero el try
            if opcion == 1:
                return Buscarporusuario()
            
            elif opcion == 2 :
                return Buscarporaplicación()
            elif opcion == 3 :
                return Buscarporfecha()
            elif opcion == 4 :
                return Retornar()
            else :
               return"Error: opcion no reconocido"
def Retornar():
    holka=0
    return RegistrodeBitácoras()


def leerarchivoR(nombreArchivo):
    if( isinstance ( nombreArchivo,str)):
        if (nombreArchivo !=""):
            archivo= open(nombreArchivo,"r")
            contenido= archivo.read()
            #contenido= archivo.readlines()
            archivo.close()
            return contenido
            
        else:
            return "ERROR EL ARRCHIVO NO DEBE SER VACIO"
    else:
        return" tipo no es texto"
def leerarchivol(nombreArchivo):
    if( isinstance ( nombreArchivo,str)):
        if (nombreArchivo !=""):
            archivo= open(nombreArchivo,"r")
            #contenido= archivo.read()
            contenido= archivo.readlines()
            archivo.close()
            return contenido
            
        else:
            return "ERROR EL ARRCHIVO NO DEBE SER VACIO"
    else:
        return" tipo no es texto"
def nombre():
    nombreAr="bitacora.txt"
    return nombreAr
#print(nombreAr)
    
"""
Nombre: escribirArchivo
Entrada: nombreArchivo, contenido
salida:no retorna pero agrega
Restricciones:
debe ser str
nombre no debe seer vacio
"""
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
        
"""
nombre: largotexto
entrada: texto
salida: vcantidad de caracteres en una cadena
retriccion: debe ser str
"""
def largoTexto (texto):
    contador=0
    if (isinstance(texto,str)):
        for caracter in texto:
            contador+=1
            
        return contador
    else:
        return "error: debe ser un texto"

"""
generador de codigos aleatorio
"""
def gencodigo():
    contador=000

    if contador==contador:
        nuevocontador=contador+1
        contador=nuevocontador

    return contador 



"""
codigo principal
"""

def Registraractividad():
    contenido=()
    codigo="f"#FALTA HACER CODIGO ALEATORIO
    txt=input("Digite la fecha de hoy")
    txt1=input(" Digite la hora actual")
    txt2=input("Digite su nombre du usuario")
    txt3= input("Digite la aplicacion correspespondiente")
    txt4 =input("Digite su mensaje")

    print ("Se esta ejecuntado el registro de la actividad")
    contenido=(codigo,txt,txt1,txt2,txt3,txt4)#se vulve str en escribir archivo
    print(contenido)
    name=nombre()
    #print (name)
    print ("Se esta ejecuntado el registro de la actividad")
    return escribirArchivo(name, contenido, "a")


def Borraractividad():
    contador=0
    name=nombre()
    lista=[]
    lista+=[leerarchivol(name)]
    codigodelete = input("digite el codigo de el registro que desea eliminar")
    for caracter in lista:
        list=[caracter]
        for elemento in list:
            if elemento[0]==codigodelete:
                continue
                
            else:
                if contador==0:
                    escribirArchivo(name,list,"w")
                    contador=1
                else:
                    escribirArchivo(name,list,"a")
    print("Se ha elimiado su registro")
    return RegistrodeBitácoras()





def Modificaractividad():
    name=nombre()
    contador=0
    lista=leerarchivol(name)
    codigoedit=input("Digite el codigo de el mensaje que desea editar")
    print("A continuacion digite su nuevo mensaje")
    fecha=input("Digite la 
    fecha de hoy en el formato DD/MM/AAAA")
    hora=input("Digite la hora de hoy en formato HH/MM/pm o am")
    usuario=input("Digite su nombre de usuario")
    aplicacion= input("Digite la aplicacion")
    mensaje= input("Digite su mensaje")
    for caracter in lista:
        list=[caracter]

        for elemento in list:
            if contador==0:
                escribirArchivo(name,"","w")
                contador=1
            if elemento[0]==codigoedit:
                nuevomensaje=(codigoedit,fecha,hora,usuario,aplicacion,mensaje)
                escribirArchivo(name,nuevomensaje,"a")
                continue 
            else:
                escribirArchivo(name,elemento,"a")
    return"Su mensaje fue modificado"
print(Modificaractividad())   






def Buscarporusuario():
    jej=0



    joam=0

def Buscarporaplicación():
    contador=0


def Buscarporfecha():
    comntadfotr=0



 