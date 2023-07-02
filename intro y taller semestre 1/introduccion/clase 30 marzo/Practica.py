"""
dividir lista
entrada: lista y pivote
salida: lista dividida
restricciones: lista debe ser entera,si elemento es diferente de entero se almacena en otra lista.
"""
def divirLista(lista,pivote):
    listaD=[]
    listap=[]
    Respuesta=[]
    if isinstance (lista,list):
        for elemento in lista:
           
            if isinstance (elemento,int):
               
            
                if elemento!=pivote:
                  
                    listap+=[elemento]
               
            

                else:
                     Respuesta+=[listap]
                     listap=[]
            else:
                 listaD+=[elemento]
        Respuesta+=[listap]        
        Respuesta+=[listaD]
        return Respuesta       
                
print(divirLista([1,2,0,3,0,4,5,"str"],0))