
class Vehiculo:
    """Inicializa la clase
    entrada: placa y horaEntrada
    restriccion: deben ser str y no estar vacios
    """
    def __init__(self,placa,hora):
        if placa !="" and isinstance(placa,str):#probar
            if hora !="" and isinstance(hora,str):#probar
                self.placa=placa
                self.horaEntrada=hora 
                self.Vehiculo=[]
                ingreso="Placa"+" "+self.placa+" "+self.horaEntrada
                self.Vehiculo+=[ingreso]   
            else:
                return "Error: debe ingresar un valor tipo str"
        else:
            return "Error: debe ingresar un valor tipo str"
    """
    Nombre: mostrar
    funcion: imprime en pantalla lo svlores ingresados
    restricciones: que no hayan valoreso variables vacios
    entrada: placa y hora"""    
    def mostrar(self):
        ingreso="Placa"+" "+self.placa+" "+self.horaEntrada
        
        return ingreso
    
class Parqueo:
    """Inicializa la clase
    entrada:Direccion,Nombre,Campos,listaDeVehiculos
    restriccion: deben ser str y no estar vacios
    """
    def __init__(self,Direccion,Nombre,Campos):
        if not Direccion !="" and isinstance(Direccion,str):#probar
            return "Error:la direccion debe ser un valor tipo str"
            
        if not Nombre !="" and isinstance(Nombre,str):#probar
            return "Error:el nombre debe ser un valor tipo str"     
        if not Campos !="" and isinstance(Campos,int):#probar
            return "Error:la cantidad de Campos debe ser un valor tipo entero"
       
        #if not telefono !="" and isinstance(telefono,str):#probar
           # return "Error:El numero de telefono debe ser un valor tipo str"
        self.parquenombre=Nombre
        self.Direccion=Direccion
        self.campos=Campos
        self.ListaDeVehiculos=[]
        #self.telefono=telefono
        
    """
    Nombre: mostrar
    funcion: imprime en pantalla los dato del parqueo
    restriccion: que no haya nada vacio
    entrada: datos
    """
    def mostrar(self):
        if not  self.Direccion !="" and isinstance(Direccion,str):#probar
            return "Error:la direccion debe ser un valor tipo str"
            
        if not self.parquenombre !="" and isinstance(self.parquenombre,str):#probar
            return "Error:el nombre debe ser un valor tipo str"     
        if not  self.campos !="" and isinstance( self.campos,str):#probar
            return "Error:la cantidad de Campos debe ser un valor tipo entero"
    
            #if not self.telefono !="" and isinstance(self.telefono,str):#probar
                #return "Error:El numero de telefono debe ser un valor tipo str"
                
        print( "Nombre: ",str(self.parquenombre))
        print("Direccion: ",str(self.Direccion))
        print("Campos disponibles: ",str(self.campos))
            #print("Telefono: ",str(self.telefono))
        
         
    """
    Nombre: datosParqueo
    funcion: imprime en pantalla los dato del parqueo
    restriccion: que no haya nada vacio
    entrada: datos
    """
    def datosParqueo(self):
        if not  self.Direccion !="" and isinstance(Direccion,str):#probar
            return "Error:la direccion debe ser un valor tipo str"
            
        if not self.parquenombre !="" and isinstance(self.parquenombre,str):#probar
            return "Error:el nombre debe ser un valor tipo str"     
        if not  self.campos !="" and isinstance( self.campos,str):#probar
            return "Error:la cantidad de Campos debe ser un valor tipo entero"
    
            
        print("Direccion: ",str(self.Direccion))
        print( "Nombre: ",str(self.parquenombre))
        print("Campos disponibles: ",str(self.campos))
            
    """
    Nombre: agregarVehículo
    funcion: agrega vehiculos al parqueo
    restriccion: que no haya nada vacio, ni se repita
    entrada: placa,horaentrada
    """ 
    def agregarVehiculo(self,placa,hora):
        if not placa !="" and isinstance(placa,str):#probar
            return "Error: debe ingresar un valor tipo str"
        if not  hora !="" and isinstance(hora,str):#probar
            return "Error: debe ingresar un valor tipo str"
        for elemento in self.ListaDeVehiculos:
            if placa==elemento.placa:
                return "Error: Este vehiculo ya se encuentra registrado"
            continue 
        ingreso=Vehiculo(placa,hora)
        if len(self.ListaDeVehiculos)<=self.campos:
            self.ListaDeVehiculos+=[ingreso]
            self.campos-=1
        else:
            return "Lo sentimos, pero ya no hay espacios disponibles"
                
    """
    Nombre: quitarVehículo
    funcion: elimina vehiculos del parqueo
    restriccion: que no haya nada vacio, y que exista 
    entrada: placa
    """    
    def quitarVehiculo(self,placa):
        existe=False
        correccion=[]
        if not placa !="" and isinstance(placa,str):
                return "Error: debe ingresar un valor tipo str"
        for elemento in self.ListaDeVehiculos:
            if placa==elemento.placa:
                existe=True
                break 
        if existe==False:
            return "Error: Este vehiculo no se encuentra registrado" 
        else:
            for elemento in self.ListaDeVehiculos:
                if placa==elemento.placa:
                    continue
                else:
                    correccion+=[elemento]
          
            self.ListaDeVehiculos=correccion
            self.campos+=1
                   
    """
    Nombre: totalVehiculos
    funcion: Cuenta cuantos vehiculos hay dentro del parqueo
    restriccion: que no haya nada vacio, y que exista 
    entrada: placa
    """  
    def totalVehiculos(self):
        if not self.ListaDeVehiculos!=[]:
            return 0  
        total=len(self.ListaDeVehiculos)
        return total
            
    """
    Nombre: mostrarVehiculos
    funcion:genera una lista con las placas de los caros registrdos en el sistema
    restriccion: que no haya nada vacio, y que exista 
    entrada: none
    """       
    def mostrarVehiculos(self):
        lista=[]
        if not self.ListaDeVehiculos!=[]:
            return "Total de vehiculos: 0 " 
        for elemento in self.ListaDeVehiculos:
         
            lista+=[str(elemento.placa)]
        return lista
