class Escuela:
    def __init__(self,nombre, dirección, teléfono,correoElectronico):
          if not nombre!="" and isinstance(nombre,str):
             return "Error, Asegurese de haber registrado un nombre de institucion"
          if not dirección!=""and isinstance(dirección,str):
             return "Error, Asegurese de haber registrado una direccion"
          if not teléfono!="":
             return "Error, Asegurese de haber registrado un numero de telefono"
        
          if not correoElectronico!=""and isinstance(correoElectronico,str):
             return "Error, Asegurese de haber registrado un correo" 
          self.nameesc=nombre
          self.dirección=dirección
          self.teléfono=teléfono
          self.correoElectronico=correoElectronico


          self.estudiantes=[]
          self.profesores=[]
          self.finalcarne="0001"
          self.graduados=[] 
    """
    nombre: mostrar
    entrada: none
    salida: muestrea de informacion en pantalla
    restriccion: que no hayan elementos vacios
    """          
    def mostrar(self):
        if not self.nameesc!="":
             return "Error, Asegurese de haber registrado un nombre de institucion"
        if not self.dirección!="":
             return "Error, Asegurese de haber registrado una direccion"
        if not self.teléfono!="":
             return "Error, Asegurese de haber registrado un numero de telefono"
        
        if not self.correoElectronico!="":
             return "Error, Asegurese de haber registrado un correo" 
        print("---------------------------------------") 
        informacion="Institucion:"+self.nameesc
        print(informacion)
        informacion="Direccion:"+self.dirección
        print(informacion)
        informacion="telefono:"+str(self.teléfono)
        print(informacion)
        informacion="correo Electronico:"+str(self.correoElectronico)
        print(informacion)
        print("---------------------------------------") 
    

    """
          nombre: agregar estudiante
          entrada: nombre,apellido1,apellido2,añomatricula,cedula,fechanacimineto
          salida informacion de estudiante
          restriccion: no paramestros diferente de str
          """
    def agregarEstudiante(self,nombre,apellido1,apellido2,añomatricula,cedula,fechanacimineto):
   
         #recordar varificar que no exista
         if isinstance(nombre,str) and nombre!="":
              if isinstance(apellido1,str)and apellido1!="":
                   if isinstance(apellido2,str) and apellido2!="":
                        if isinstance(cedula,str) and cedula!="":
                             if isinstance(fechanacimineto,str)and fechanacimineto!="":
                                    if añomatricula!="":
                                        if self.estudiantes==[]:
                                             carnet=canets(self,fechanacimineto,str(añomatricula))
                                             estudiante=Estudiante(nombre,apellido1,apellido2,str(añomatricula),cedula,fechanacimineto,carnet)
                                             self.estudiantes+=[estudiante]
                                             #self.estudiantes[-1].mostrar()
                                             
                                        else:      
                                             for doc in self.estudiantes:
                                                  if cedula==doc.cedula:
                                                       return "Error:la cedula ingresada ya se encuentra en el registro"
                                                  
                                             carnet=canets(self,fechanacimineto,str(añomatricula))
                                             estudiante=Estudiante(nombre,apellido1,apellido2,str(añomatricula),cedula,fechanacimineto,carnet)
                                             self.estudiantes+=[estudiante]
                                          
                                                       
                                                    
                                             
                                    
                                  
         
                             else:
                                  return"debe ingresar valores de caracter str"           
                        else:
                            return"debe ingresar valores de caracter str"   
                   else:
                        return"debe ingresar valores de caracter str"   
              else:
                return"debe ingresar valores de caracter str"   

         else:
            return"debe ingresar valores de caracter str"   
        
     
 
    """
    Nombre: buscar estudiante
    entrada: identificacion
    salida coincidencias con la identificacion de estudiantes
    restriccion: que no ingrese valores vacios ni diferente a formato str"""
    def  buscarEstudiante(self,identificacion):
         if identificacion!="":
            if isinstance(identificacion,str) and identificacion!="":
                 for elemento in self.estudiantes:
                      if identificacion==elemento.carnet:
                              return elemento.mostrar()
                 
                 return"Error la cedula ingresada no se encuentra en la matricula"
            else:
                return "Error: debe ingresar en formato str la cedula"  
         else:
              return "Error: debe ingresar alguna cedula y no dejar el espacio vacio"
         
    """
    nombre: agregar profesor
    entrada:nombre, apellido1, apellido2, cedula,profesion
    salida: se agrega el profesor
    restricciones no caracteres vacios ni diferente de str 
    """
    def  agregarProfesor(self,nombre, apellido1, apellido2, cedula,profesion ):
          if isinstance(nombre,str) and nombre!="":
              if isinstance(apellido1,str) and apellido1!="":
                   if isinstance(apellido2,str) and apellido2!="":
                        if isinstance(cedula,str) and cedula !="":
                             if isinstance(profesion,str) and profesion!="":
                                   profe=Profesor( nombre, apellido1, apellido2, cedula,profesion)
                                   self.profesores+=[profe]
                             else:
                                  return "Error: debe ingresar valores de caracter str y no vacios"
                        else:
                              return "Error: debe ingresar valores de caracter str y no vacios"    

                   else:
                        return "Error: debe ingresar valores de caracter str y no vacios"
              else:
                    return "Error: debe ingresar valores de caracter str y no vacios"
          else:
                return "Error: debe ingresar valores de caracter str y no vacios"  
          
    


    """
    Nombre: buscar profesor
    entrada: cedula
    salida coincidencias con la identificacion de profesores
    restriccion: que no ingrese valores vacios ni diferente a formato str"""
    def  buscarProfesor(self,cedula):
         if cedula!="":
            if isinstance(cedula,str):
                 for elemento in self.profesores:
                      if cedula==elemento.cedula:
                             return elemento.mostrar()
                 return "Error la cedula ingresada no se encuentra en la matricula"
            else:
                return "Error: debe ingresar en formato str la cedula"  
         else:
              return "Error: debe ingresar alguna cedula y no dejar el espacio vacio"
         
    """
    Nombre: mostrarProfesores
    entrada: none
    salida:profesores registrados
    restriccion: que no hayan valores vacios"""
    def  mostrarProfesores(self):

        if not self.profesores!=[]:
            return "Error: no se encuentran pacientes activos"
        
        for elemento in self.profesores:
             elemento.mostrar()
    """
     Nombre: mostrarEstudianteMatriculados
     entrada: año
     salida:estudiantes registrados
     restriccion: que no hayan valores vacios"""    
    def mostrarEstudianteMatriculados(self,anio):
        if not self.estudiantes!=[]:
            return "Error: no se encuentran estudiantes activos"
        
        for elemento in self.estudiantes:
            año=elemento.carnet[0:4]
            if (str(anio)==año): 
                 if elemento==self.estudiantes[-1]:
                    return elemento.mostrar()
                 else:
                       elemento.mostrar()                 
        return "No se encuentran estuidiantes maticulados en este año lectivo"

    """
     Nombre: mostrarEstudianteMatriculados
     entrada: carne,añodegraduacion
     salida: se elimina un estudiante y se genera estadisticas
     restriccion: que no hayan valores vacios"""                          
    def graduarEstudiante(self,carne,añodegraduacion):
         coreccion=[]
         estudiante=[]
         self.añodegraduacion=añodegraduacion
         if carne!="":
              if isinstance(carne,str):
                   if añodegraduacion!="":
                        if isinstance(añodegraduacion,int):
                             for elemento in self.estudiantes:
                                  if carne==elemento.carnet:
                                       estudiante+=[str(elemento.carnet)]
                                       estudiante+=[str(elemento.nombre)]
                                       estudiante+=[str(añodegraduacion)]
                                       diferencia=int(self.añodegraduacion)-int(elemento.fechaNacimiento[6:])
                                       estudiante+=[diferencia]
                                       estudio=int(self.añodegraduacion)-int(elemento.añomatricula)
                                       estudiante+=[estudio]
                                       self.graduados+=[estudiante]
                                  else:
                                       coreccion+=[elemento]
                                       self.estudiantes=coreccion 
    """
     Nombre: tiempoGraduacion
     entrada: none
     salida: retorna la estadistica de estudiantes graduados
     restriccion:que no haya valores vacios """            
    def tiempoGraduacion(self):
          if not self.graduados!=[]:
               return "No se encuentran estudiantes graduados"
               
               
          print("Identificación | Nombre completo    | Año Graduación | Edad actual | Años Estudio")
          for elemento in self.graduados:
               print(elemento[0],"      ",elemento[1],"       ",elemento[2],"           ",elemento[3],"           ",elemento[4])
          
class Estudiante:
    def __init__(self,nombre,apellido1,apellido2,añomatricula,cedula,fechanacimineto,carnet):
         if not nombre!="" and isinstance(nombre,str):
             return "Error, Asegurese de haber registrado un nombre"
         if not apellido1!=""and isinstance(apellido1,str):
             return "Error, Asegurese de haber registrado un apellido"
         if not cedula!=""and isinstance(cedula,str):
             return "Error, Asegurese de haber registrado un numero de cedula"
        
         if not apellido2!=""and isinstance(apellido2,str):
             return "Error, Asegurese de haber registrado un apellido" 
         if not fechanacimineto!=""and isinstance(fechanacimineto,str):
             return "Error, Asegurese de haber registrado una fecha de nacimiento" 
        
         if not añomatricula!="":
             return "Error, Asegurese de haber registrado un año de matricula" 
        
         self.nombre=str(nombre+" "+apellido1+" "+apellido2)
         self.añomatricula=añomatricula
         self.cedula=cedula
         self.fechaNacimiento=fechanacimineto
         
         self.edad=int(self.añomatricula)-int(self.fechaNacimiento[6:])
       
         self.carnet=carnet

    """
    nombre: mostrar
    entrada: none
    salida: muestrea de informacion en pantalla
    restriccion: que no hayn elementos vacios
    """          
    def mostrar(self):
        if not self.nombre!="":
             return "Error, Asegurese de haber registrado estudiantes"
        if not self.carnet!="":
             return "Error, Asegurese de haber registrado estudiantes"
        if not self.edad!="":
             return "Error, Asegurese de haber registrado estudiantes"
        
        print("-----------------------------------")
        informacion="Nombre estudiante:"+self.nombre
        print(informacion)
        #informacion+="Año de matricula:"+self.añomatricula+"\n"
        #informacion+="cedula:"+str(self.cedula)+"\n"
        #informacion+="fecha nacimiento:"+str(self.fechaNacimiento)+"\n"
        informacion="Carnet:"+str(self.carnet)
        print(informacion)
        informacion="Edad:"+str(self.edad)
        print(informacion)
        print("-----------------------------------")
       
        
        #print(informacion)

     
class Profesor:
    def __init__(self, nombre, apellido1, apellido2, cedula,profesion ):
         if not nombre!="" and isinstance(nombre,str):
             return "Error, Asegurese de haber registrado un nombre"
        
         if not apellido1!=""and isinstance(apellido1,str):
             return "Error, Asegurese de haber registrado un apellido"
         if not cedula!=""and isinstance(cedula,str):
             return "Error, Asegurese de haber registrado un numero de cedula"
        
         if not apellido2!=""and isinstance(apellido2,str):
             return "Error, Asegurese de haber registrado un apellido" 
         if not profesion!=""and isinstance(profesion,str):
             return "Error, Asegurese de haber registrado la profesion" 
         
        
         self.nombre=str(nombre+" "+apellido1+" "+apellido2)
         self.profesion=profesion
         self.cedula=cedula
     
    """
    nombre: mostrar
    entrada: none
    salida: muestrea de informacion en pantalla
    restriccion: que no hayn elementos vacios
    """     
    def mostrar(self):
        if not self.nombre!="":
             return "Error, Asegurese de haber registrado educadores"
        if not self.profesion!="":
             return "Error, Asegurese de haber registrado educadores"
        if not self.cedula!="":
             return "Error, Asegurese de haber registrado educadores"
        print("-----------------------------------")
        informacion="Nombre Profesor : "+ " "+self.nombre
        print(informacion)
        informacion="profesion : "+ " "+ self.profesion
        print(informacion)
        informacion="cedula : "+ " "+str(self.cedula)
        print(informacion)
        print("-----------------------------------")
"""
Nombre:canets
entrada:fechanacimineto,añomatricula
salida: formacion de carnet
retriccion: que no hayan elementos vacios
"""        
def canets(self,fechanacimineto,añomatricula):
     if not añomatricula!="":
          return "Debe ingresar un año de matricula valido"
     carnet=""
     carnet=str(añomatricula)+self.finalcarne
     nueva=""
     change=self.finalcarne
     variable=int(change[-1])+1
     change=str([change[:-1]])
     for elemento in change:
          try:
               elemento=int(elemento)
               if (elemento,int):
                    nueva+=str(elemento)
          except:
                  continue 
     nueva+=str(variable)    
     self.finalcarne=str(nueva)
     return carnet

    
escuela = Escuela("Liceo La Esperanza", "San José", "85859966", "laescuela@sanjose.com")
escuela.agregarEstudiante("Luisa", "Lopez", "Campos", 2019, "354650022", "20/02/2012")
escuela.agregarEstudiante("Maria", "Jimenez", "Moya", 2020, "354651122", "20/03/2013")
escuela.buscarEstudiante( "20190001")
escuela.agregarProfesor("Mario", "Carmona", "Perez", "801230456", "Educador")
escuela.buscarProfesor("801230456") 
escuela.mostrarProfesores()
escuela.mostrarEstudianteMatriculados(2020)
escuela.graduarEstudiante("20190001", 2023)
escuela.graduarEstudiante("20200002", 2023)
escuela.tiempoGraduacion()

