
class Paciente:
    def __init__(self,cedulapaciente,fecha,padecimineto,ceduladoctor):
         self.cedulapaciente=cedulapaciente
         self.fecha=fecha
         self.padecimineto=padecimineto
         self.ceduladoctor=ceduladoctor
         
    def mostrar(self):
        informacion="cedula paciente:"+self.cedulapaciente+","
        informacion+="fecha:"+self.fecha+","
        informacion+="padecimiento:"+str(self.padecimineto)+","
        informacion+="cedula doctor:"+str(self.ceduladoctor)
    
class Expediente:
    def __init__(self,nombre,apellido,cedula,edad):
         self.nombre=nombre
         self.apellido=apellido
         self.cedula=cedula
         self.edad=edad
    def mostrar(self):
        informacion="Nombre:"+self.nombre+","
        informacion+="Apellido:"+self.apellido+","
        informacion+="Cedula:"+str(self.cedula)+","
        informacion+="Edad:"+str(self.edad)

        return informacion
class Doctor:
    def __init__(self,nombre,apellido,cedula,especialidad):
         self.nombre=nombre
         self.apellido=apellido
         self.cedula=cedula
         self.especialidad=especialidad
    def mostrar(self):
        informacion="Nombre:"+self.nombre+","
        informacion+="Apellido:"+self.apellido+","
        informacion+="Cedula:"+str(self.cedula)+","
        informacion+="especialidad:"+str(self.especialidad)
        return informacion


class clinica:
    def __init__(self,nombreClinica,Direccion,Telefono,email):
        self.nombreClinica=nombreClinica
        self.Direccion=Direccion
        self.telefono=Telefono
        self.correoElectronico=email
        self.listapacientes=[]
        self.listadoctor=[]
        self.listaExpediente=[]    
    def mostrar(self):
        informacion="Nombre:"+self.nombreClinica+","
        informacion+="Direccion:"+self.Direccion+","
        informacion+="telefono:"+str(self.telefono)+","
        informacion+="correoElectronico:"+str(self.correoElectronico)
        return informacion
    def agregarExpediente(self,nombre,apellido,cedula,edad):
        #validaciones
         
        for exp in self.listaExpediente:
            if cedula==exp.cedula:
                return "Error:cedula existente"
        
        expediente=Expediente(nombre,apellido,cedula,edad)
        self.listaExpediente+=[expediente]
    def buscarExpediente(self,cedula):
        if isinstance(cedula,str):
            for elemento in self.listaExpediente:
                if cedula==elemento.cedula:
                   
                    return elemento.mostrar()
               
        else:
            return "Error: debe ingresar un str" 
               
    def agregardoctor(self,nombre,apellido,cedula,especialidad):
        #validaciones
         
        for doc in self.listadoctor:
            if cedula==doc.cedula:
                return "Error:El doctor ya se encuentra registrado"         
        doctor=Doctor(nombre,apellido,cedula,especialidad)
        self.listadoctor+=[doctor]


    def buscardoctor(self,cedula):
        if isinstance(cedula,str):
            for doc in self.listadoctor:
                if cedula==doc.cedula:
                    continue
                else:
                    return "Error:El doctor NO se encuentra registrado"            
        
            for elemento in self.listadoctor:
                if cedula==elemento.cedula:
                    return elemento.mostrar()
    def regitrarpaciente(self,cedulaPaciente,fecha,padecimiento,cedulaDoctor):
        existedoc=False
        existepac=False
        existe=False

        if isinstance(cedulaPaciente,str):
            if self.listapacientes==[]:
                 existe=True
            for exp in self.listapacientes:
                if cedulaPaciente==exp.cedula:
                    existe=True
                    break
        if not existe:
            return "Error: paciente registrado previamente"    
             
                         

        if isinstance(cedulaPaciente,str):
            for elemento in self.listaExpediente:
                if cedulaPaciente==elemento.cedula:
                    existepac=True
                    break
        if not existepac:
            return "Error:No existe con dicha cedula"
           
        if isinstance(cedulaDoctor,str):
            for elemento in self.listadoctor:
                if cedulaDoctor==elemento.cedula:
                  
                    existedoc=True
                    break    

        if not existedoc:
            return "Error:No existe con dicha cedula1"
        
                           
        paciente=Paciente(cedulaPaciente,fecha,padecimiento,cedulaDoctor)
        self.listapacientes+=[paciente]


    def darAlta(self,cedula):
        delete=[]
        if isinstance(cedula,str):
            for doc in self.listapacientes:
                if cedula==doc.cedulapaciente:
                    continue
                else:
                    return "Error:la cedula ingresada no se encuentra en el registro"

            for elemento in self.listapacientes:
                if cedula==elemento.cedulapaciente:
                    continue
                else:
                    delete+=[elemento]

            self.listapacientes=[]
            for elemento in delete:
                 self.listapacientes+=[elemento]

    def mostrarpaciente(self):

        if not self.listapacientes!=[]:
            return "Error: no se encuentran pacientes activos"
        
        for elemento in self.listapacientes:
            return elemento.mostrar()
