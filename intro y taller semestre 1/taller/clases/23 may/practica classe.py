class calculadora:
    
    def __init__(self):
       self.operador1=0
       self.operador2=0
       self.Resultado=0
       self.memoria11=0
       self.memoria22=0
       self.num=""
       
       
    def guardarOperador1(self,operador1):
        if isinstance(operador1,int):
                self.operador1=operador1
                print(operador1)
        else: 
            return "Error: debe ingresar valores enteros"
           
    def guardarOperador2(self,operador2):
        if isinstance(operador2,int):
                self.operador2=operador2
               
        else: 
            return "Error: debe ingresar valores enteros"
               
    def suma(self,operador1,operador2):
        respuesta=operador1+operador2
        self.Respuesta=respuesta
        
    def resta(self,operador1,operador2):
        respuesta=operador1-operador2
        self.Respuesta=respuesta
        
    def multiplicacion(self,operador1,operador2):
        respuesta=operador1*operador2
        self.Respuesta=respuesta
        
        
    def division(self,operador1,operador2):
        if isinstance(operador1>0):
            if isinstance(operador2>0):
                respuesta=operador1/operador2
                self.Respuesta=respuesta
            else:
                return"Error: el operador 2 no puede ser menor o igual a 0"        
        else:
                return"Error: el operador 2 no puede ser menor o igual a 0"       
       
    def fibonacci(self,operador1):
        # fib-1+fib-2
        if not isinstance(operador1,int):
            return"El numero debe ser entero"
        if not operador1>=0:
            return "El numero debe ser mayor a 0"
        
        return self.fibonachi_aux(operador1)

    def fibonachi_aux(self, operador1):
    
        if operador1==0:
            return 0
        elif operador1==1: 
            return 1     
        else:
            
            x= self.fibonachi_aux(operador1-1)+self.fibonachi_aux(operador1-2)
            self.Respuesta=x
    def factorial(self,operando1):
        x= self.factorial1(operando1)   
    def factorial1(self,operando1):
        if operando1 == 0:
            return 1
        else:
            return self.factorial1(operando1-1) * operando1  
          
    def sumatoria(self,operador1):
        while self.operador1!=0:
            respuesta+=self.operador
            self.operador-1
        self.Respuesta=respuesta
    def potencia(self,operando1,operando2):
        respuesta=operando1**operando2
        self.Respuesta=respuesta
    def mostrarResultado(self):
            rep=self.Respuesta
            return rep
    def memoria1(self):
        resp=self.Respuesta
        self.memoria11=resp
    def memoria2(self):
        resp=self.Respuesta
        self.memoria22=resp
    def verMemoria(self,num):
            if num=="memoria1":
                x=self.memoria11
                return x
            else:
                x=self.memoria22
                return x
    def borrarResultado(self):
        self.Respuesta=0
        
    def BorrarMemoria(self,num):
        if num=="memoria1":
                self.memoria11=0
                
        else:
            self.memoria22=0
            
class Archivo:
    def __init__(self):
         self.NombreArchivo="" 
         self.punteroArchivo=""
         self.contenido=""
    def Archivo(self,Nombre):
        
        self.NombreArchivo=Nombre
    def abrirArchivo(self,modo):
        if (modo != ""):
            if (isinstance(modo,str)):
                mi_tupla=("readlines","read") 
                name=self.NombreArchivo
                if modo in mi_tupla:
                    archivo =open(name, mode= "r")
                    self.contenido = archivo.modo()
                    archivo.close()
                else:
                    return "error el modo indicado no es correcto"
   
       
            else:
                return" tipo no es texto"
            
        else:
            return "ERROR EL ARRCHIVO NO DEBE SER VACIO"
    def cerrarArchivo(self):
        name=self.NombreArchivo
        archivo =open(name, mode= "r")
        archivo.close()
    def verContenido(self):
        x=self.contenido
        return x 
    