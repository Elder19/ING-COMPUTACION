"""
nombre: descomponerNumeros
entrada:lista
salida: sublistas 
restricciones mayor a cero, si es negativo se convierte a positivo, misma longitud
"""


def descomponerNumeros(x,y):
    if x<0:
        x=x*-1
    if y<0:
        y=y*-1
    long1=largo(x)
    long2=largo(y)
    if not long1==long2:
        return "El largo no cumple con los parametros"
    return descomp2(x,y,[],[])
   
def descomp2(x,y,listap,listai):
    n1=x%10
    n2=y%10
    if n1!=0 and n1!=0:
        if n2%2==0:
            listap+=[n2]
        else:
            listai+=[n2]
        if n1%2==0:
            listap+=[n1]
        else:
            listai+=[n1]
        return descomp2(x//10,y//10,listap,listai)    
    else:
        total=[listap,listai]
        return total
def largolisa(x):
    if x!=[]:
            x=x[1:]
            return 1+largolisa(x)

    else:
        return 0   
def largo(x):
   
    if x<=9:
        return 1
    else:
        return 1+largo(x//10)

        
"""
nombre: eliminarpares
salida: lista sin pares
entrada: lista
restricciones: 
Esto programarlo con recursión de cola
 Su recorrido será de izquierda a derecha
 Los números pueden ser enteros positivos o negativos
 La lista debe tener al menos dos elemento
 """    
def eliminarPares(num):
    largol=largolisa(num)
    if not(largol>=2):
        return "Error el numero ni puede ser menor a dos elementos"
    
    return elimina2(num,0,[],largol)
def elimina2(num,cont,lista,largol):
    if cont<largol:
        if num[cont]%2==0:
            return  elimina2(num,cont+1,lista,largol)
        
        else:
            lista+=[num[cont]]
            return  elimina2(num,cont+1,lista,largol)
    else:
        return lista
        
    
def calcular(num):
    carry=0
    if not (num<=0):
        num=num*-1
        carry=1
    if isinstance (num,int):
        return calc2(num,0)
        
    
def calc2(num,n2):
    
    n1=
    v=0
    
    
    
    
    
    
    
    
    
    
def adyancenteImpar(num):
    long=largo(num)
    if long%2==0:
        x=i2(num)
        return True
    else:
        return "Error"
    
    
    
def i2(num):
    if num!=0:
        n1=num%10
        num=num//10
        n2=num%10
        r=n1+n2
        if r%2!=0:
            return True+i2(num//10)
        else:
            return False
    return True    
        
print(eliminarPares( [-23, 5, 8, 23] ))       

print(descomponerNumeros(2563,1002))    