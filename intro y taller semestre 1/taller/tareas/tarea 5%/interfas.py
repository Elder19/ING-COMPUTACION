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
            elif opcion == 3 :
                return Cantidaddemensajes()
            elif opcion == 4 :
                return Guardarmensajes()
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
            elif opcion == 4 :
                return Vertodaslasactividades()
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
        else :  #el else se ejecuta cuando no genero el try
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
    return RegistrodeBitácoras()

    
    
    

    

