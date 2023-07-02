class admin:
    def __init__(self,nombre,telefono,direccion,correo):
        
        self.nombreestablecimineto=nombre
        self.telefono=telefono
        self.direccion=direccion
        self.correo=correo
        self.canchas=[]
        self.clientes=[]
        self.identificador = 0
  
        

    def mostrar(self):
        informacion= "Nombre"+str(self.nombreestablecimineto)+"\n"
        informacion+="Numero telefono"+str(self.telefono)+"\n"
        informacion+="Direccion: "+str(self.direccion)
        informacion+="correo: "+str(self.correo)
        print(informacion)

        #return informacion

    def crear_cancha(self,preciohora,nombrecancha):
        canchas=Cancha("keep",1000,self.identificador)
        self.canchas+=[canchas]
        
    def crear_cliente(self,cedula, nombre ,telefono,correo):
            if not cedula=="" and isinstance(cedula,str):
                return "Error: asefurese de ingresar cedulas validas"
            if not nombre=="" and isinstance(nombre,str):
                return "Error: asefurese de ingresar nombres validas"
            if not telefono=="" and isinstance(telefono,str):
                return "Error: asefurese de ingresar telefonos validas"
            if not correo=="" and isinstance(correo,str):
                return "Error: asefurese de ingresar correos validas"
            
            if not self.clientes!=[]:
                cliente=Cliente(nombre,cedula,telefono,correo)
                self.clientes+=[cliente]
            else:
                for elemento in self.clientes:
                    if cedula==elemento.cedula:
                        return "Error cliente ya registrado"
                
                cliente=Cliente(nombre,cedula,telefono,correo)
                self.clientes+=[cliente]        
                
                
            
            
        
        
        
class Cancha:
    
    def __init__(self,nombre,precio,ident):
  
        self.nombrecancha=  str(nombre)+str(ident)
        self.precio=precio
        admin.identificador += 1

class Cliente:
    def __init__(self,nombre, cedula , telefono,correo):
        self.nombre=nombre
        self.cedula=cedula
        self.telefono=telefono
        self.correo=correo
    def mostrar(self):
        informacion="Nombre: "+str(self.nombre)+"\n"
        informacion+="Cedula: "+ str(self.cedula)+"\n"
        informacion+="Telefono: "+str(self.telefono)+"\n"
        informacion+="Correo: "+str(self.correo)
