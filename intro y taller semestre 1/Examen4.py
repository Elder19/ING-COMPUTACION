""" correcciones hechas
1) Error en el init de salaFutbol, se aplico mal el if not 
2) en mostrar chocan los nombres de codigo (mostrar) """
class SalaFutbol:

        def __init__(self,nombreEstablecimiento,telefono,direccion,correoElectronico):
            if not nombreEstablecimiento!="" and  isinstance(nombreEstablecimiento,str):
                print ("error debe ingresar un nombre de establecimineto")
            if not telefono!="" and isinstance(telefono,int):
                print ("Error debe ingresar un numero telefononico")
            if not direccion!="" and isinstance(direccion,str):
                print ("Error debe ingresar una direccion")
            if not correoElectronico!="" and isinstance(correoElectronico,str):
                print ("Error debe registrar un correo electronico")
            acceso=False
            for elemento in correoElectronico:
                if elemento=="@":
                    acceso=True
                    break
            if not acceso!=False:
                print ("Error: La cuenta de correo no tiene formato correcto")
            self.nombrefut=nombreEstablecimiento
            self.telefono=telefono
            self.direccion=direccion
            self.email=correoElectronico
          

            # listas de mas

            self.listaCanchas=[]
            self.listacliente=[]
            self.canchasreservadas=[]
        """
        nombre: mostrar
        funcion:retornar la informacion que haya ingresado al constructor
        """

        def mostrarclase1(self):
            informacion="--------------------------------------"
            informacion+="Nombre: "+self.nombrefut +"\n"
            informacion+="Telefono: "+str(self.telefono)+"\n"
            informacion+="Direccion: "+str(self.direccion)+"\n"
            informacion+="Correo Electronico: "+str(self.email)+"\n"
            informacion+="Horario: L a D de 1 a 10 pm"+"\n" 
            informacion+="--------------------------------------"
            print(informacion)
            #return informacion
        """
            nombre: crear cancha
            entrada: precio,capacidad
            salida: cahchas creadas
            restriccion: que ingresen numeros enteros
            """
        def crearCancha(self,precio,capacidad):
            if not precio!="" and precio>0:
                return"Error: Los valores deben ser numéricos enteros" 
            if not capacidad!="" and isinstance(capacidad,int) and capacidad>0:
                return ("Error: Los valores deben ser numéricos enteros")
            cancha=Cancha(precio,capacidad)
            self.listaCanchas+=[cancha]
        """
            nombre: mostrarCanchas
            entrada: none
            salida: cahchas creadas
            restriccion: que existan canchas creadas previamente
            """   
        def mostrarCanchas(self):
            if self.listaCanchas==[]:
                return "Error un no se crean canchas"
            for elemento in self.listaCanchas:
                #print(elemento)
                elemento.mostrar()

        """
            nombre: crearCliente
            entrada: cedula,nombre,apellido1, apellido2,telefono,correo
            salida:ingreso de cliente al sistema
            restriccion: que los elementos no esten vacis y cumplan con su formato
            """  

        def crearCliente(self,cedula,nombre,apellido1, apellido2,telefono,correo):
            acceso=True
            if not cedula!="":
                return ("Error la cedula de cliente nom cumple con los parametros")
            if not isinstance(cedula,str):
                return ("Error la cedula de cliente nom cumple con los parametros"  )
            if not len(cedula)==9:
                return ("Error la cedula de cliente nom cumple con los parametros")
            
            if not telefono!="":
                return ("Error: asegurese de ingresar un numero de telefono")
                
            if not isinstance(telefono,int):
                    return ("Error: asegurese de ingresar un numero de telefono")
                
            if not nombre!="":
                return ("error debe ingresar un nombre valido ")
            
            if not isinstance(nombre,str):
                return "error debe ingresar un nombre valido "
            if not correo!="":
                return "Error: debe ingresar un correo valido"
            
            if not isinstance(correo,str):
                return "Error: debe ingresar un correo valido"
            if not apellido1!="" :
                return "error debe ingresar un apellido valido "
            if not isinstance(apellido1,str):
                return "error debe ingresar un apellido valido "
            if not apellido2!="" :
                return "error debe ingresar un nombre valido "
            
            if not isinstance(apellido2,str):
                    return "error debe ingresar un nombre valido "
            if self.listacliente==[]:
                x="Puta"
                return( x)
                
                
            else:
                 for elemento in self.listacliente:
                    if cedula==elemento.cedula:
                        return "Este cliente ya existe en la base de datos"
            for elemento in correo:
                    if elemento=="@":
                        acceso=False
                    
                       
            
            if not acceso !=True:
                 return "Error: La cuenta de correo no tiene formato correcto"
            cliente=Cliente(cedula,nombre,apellido1, apellido2,telefono,correo)
            self.listacliente+=[cliente]
        """
            nombre: buscarCliente
            entrada: cedula
            salida:retorna infomacioon del cliente
            restriccion: que los elementos no esten vacios y cumplan con su formato
            """ 
        def buscarCliente(self,cedula):
             
            if not cedula=="" and  isinstance(cedula,str) and len(cedula)==9:
                    return( "Error la cedula de cliente nom cumple con los parametros")
            if self.listacliente==[]:
               return ("Error: no se han igresado clientes")
            for elemento in self.listacliente:
                    if cedula==elemento.cedula:
                        return elemento.mostrar()
            return ("Error: Cliente no encontrado")
        
        """
            nombre: modificarCliente
            entrada: cedula,nombre,apellido1, apellido2,telefono,correo
            salida: modifica los clientes
            restriccion: none
            """ 

        def  modificarCliente(self,cedula,nombre,apellido1, apellido2,telefono,correo):
             for elemento in self.listacliente:
                  if cedula==elemento.cedula:
                        if nombre!="":
                            elemento.nombre=nombre
                        if apellido1!="":
                             elemento.apellido1=apellido1
                        if apellido2!="":
                             elemento.apellido2=apellido2
                        if telefono!="":
                             elemento.telefono=telefono
                        if correo!="":
                             for elemento in correo:
                                if elemento=="@":
                                   elemento.correo=correo   
                                else:
                                    return "Error: La cuenta de correo no tiene formato correcto"


        """
            nombre: mostrarClientes
            entrada: cedula,nombre,apellido1, apellido2,telefono,correo
            salida: modifica los clientes
            restriccion: none
            """                                                 
        def mostrarClientes(self):
             if self.listacliente!=[]:
                  for elemento in self.listacliente:
                       elemento.mostrar()
             
        """
            nombre: reservarCancha
            entrada: cedula,identificador,fecha,hora_inicio,horas
            salida: reserva canchas
            restriccion: que no se ingresen valores vacios y que cumplan con su formato
            """  
        def reservarCancha(self,cedula,identificador,fecha,hora_inicio,horas):
            if not cedula=="" and  isinstance(cedula,str):
                return ("Error: debe ingresar una cedula valida")
            if not identificador=="" and isinstance(identificador,int):
                return ("error debe ingresar un identificador valido")
            if not fecha=="" and isinstance(fecha,str):
                return ("Una fecha valida")
            if not hora_inicio=="" and isinstance(hora_inicio,int) and  isinstance(horas,int)and horas!="":
                return "error debe ingresar un nombre de establecimineto"
            existe2=False
            existe=False
            for elemento in self.listacliente:
                 if cedula==elemento.cedula:
                      existe=True
            for elemento in self.canchasreservadas:
                 if elemento.identificador==identificador:
                      existe2=True
            if existe==True and existe2==True:     
            
                for elemento in self.listaCanchas:
                    if identificador==elemento.identificador: 
                        if self.canchasreservadas==[]:
                            reserva=Reserva(cedula,identificador,fecha,hora_inicio,horas)
                            

                        else:
                            for caracter in self.canchasreservadas:
                                if identificador==caracter.identificador:
                                    if fecha==caracter.fecha:
                                        if hora_inicio==caracter.hora_inicio:
                                                return "La cancha ya se encuentra reservada"
                                        else: 
                                                if hora_inicio<caracter.hora_inicio:
                                                    if hora_inicio+horas<caracter.hora_inicio:  
                                                        reserva=Reserva(cedula,identificador,fecha,hora_inicio,horas)
                                                elif  hora_inicio>caracter.hora_inicio:
                                                        if hora_inicio+horas>caracter.hora_inicio:  
                                                            reserva=Reserva(cedula,identificador,fecha,hora_inicio,horas)
            else:
                 return "El cliente no se encuentra registrado o la cancha no existe"
        """
            nombre: mostrarReserva
            entrada: identificador
            salida: reservas reñacionadas a e identificador
            restriccion:que el identicador no este vacio
            """  
        def mostrarReserva(self,identificador):
             if identificador=="":
                  return "Debe ingresar in identificador"
             if self.reservarCancha==[]:
                  return "No se han hecho reservaciones" 
             for elemento in  self.reservarCancha:
                  if elemento.identificador==identificador:
                       elemento.mostrar()
                  

        """
            nombre: borrarReserva
            entrada: numero
            salida: elimina reservas
            restriccion:que el codigo no este vacio
            """  
        def borrarReserva(self,numero):
             nueva=[]
             if numero=="":
                  return "El codigo ingresado no es valido o esta vacio"
             for elemento in self.canchasreservadas:
                  if numero==elemento.code:
                       continue
                  else:
                       nueva+=[elemento]
             self.canchasreservadas=nueva
       

class Reserva:
      codigo=1000
      def __init__(self,cedula,identificador,fecha,hora_inicio,horas):
        
            self.identificador=identificador
            self.precio=1000*horas
            self.cedula=cedula
            self.fecha=fecha
            self.horas=horas
            self.hora_inicio=hora_inicio
            self.code=self.codigo

            SalaFutbol.reservarCancha+=[ self.identificador, self.precio,self.cedula,self.fecha, self.horas, self.hora_inicio,self.code]
            self.codigo+=1
      """
        nombre: mostrar
        funcion:retornar la informacion que haya ingresado al constructor
        """

      def mostrar(self):
    
        informacion= str(self.identificador) +"\n"
        informacion+="Precio : "+str(self.precio)+"\n"
        informacion+="fecha:  "+str(self.fecha)+"\n"
        informacion+="horas : "+str(self.horas)+"\n"
        informacion+="hora_inicio:  "+str(self.hora_inicio)+"\n"

        informacion+="CODIGO : "+str(self.codigo)+"\n"
        return(informacion)
            #return informacion  
       
class Cancha:
    identificador=0
    def __init__(self,precio,capacidad):
        
            self.identificador+=1
            self.precio=precio*capacidad
            self.capacidad=capacidad
         
            Cancha.identificador+=1
    """
        nombre: mostrar
        funcion:retornar la informacion que haya ingresado al constructor
        """

    def mostrar(self):
        informacion="--------------------------------------"+"\n"
        informacion+="Numero de cancha: "+str(self.identificador)+"\n"
        informacion+="Precio : "+str(self.precio)+"\n"
        informacion+="capacidad:  "+str(self.capacidad)+"\n"
        
        
        informacion+="--------------------------------------"
        print(informacion)
                    
class Cliente:
    def __init__(self,cedula,nombre,apellido1, apellido2,telefono,correo):
          self.cedula=cedula
          self.nombre=nombre
          self.apellido1=apellido1
          self.apellido2=apellido2
          self.telefono=telefono
          self.correo=correo

    """
        nombre: mostrar
        funcion:retornar la informacion que haya ingresado al constructor
        """

    def mostrar(self):
       
        informacion= "Nombre establecimineto: "+str(self.nombre)+" " +str(self.apellido1)+" "+str(self.apellido2)+"\n"
        informacion+="cedula : "+str(self.cedula)+"\n"
        informacion+="telefono:  "+str(self.telefono)+"\n"
        informacion+="Correo electronico :  "+str(self.correo)+"\n"
        return(informacion)
            #return informacion
        


