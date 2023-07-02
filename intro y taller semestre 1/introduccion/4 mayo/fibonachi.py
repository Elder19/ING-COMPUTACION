"""
nombre:fibonachi
entada n entero
salida:suma-
restriccion: n es entero
"""
def fibonachi(N):# fib-1+fib-2
    if not isinstance(N,int):
        return"El numero debe ser entero"
    if not N>=0:
        return "El numero debe ser mayor a 0"
    return fibonachi_aux(N)

def fibonachi_aux(N):
   
    if N==0:
        return 0
    elif N==1: 
        return 1     
    else:
        
        return fibonachi_aux(N-1)+fibonachi_aux(N-2)




"""
nombre esprimo
entrada num y cont
salida: true false
restriccion entero"""

def esprimo(num):
    if not(num>0):
        return "ERROR debe ingresr numeros mayores a 0"
    if not(num,int):
        return "error debe ingresar numeros enteros"
    cont=1
    return esprimo2(num,cont)
def esprimo2(num,cont):
        if cont<num:
        
            if num%2!=0:
                return esprimo2(num,cont+1)
            elif cont==1:
                return esprimo2(num,cont+1)
            
            else: 
                return False
        return True
        

"""
nombre: contruir pares
entrada: n
salida: true false
restriccion enteros
"""
def contruirpares(num):
    if not(num>0):
        return "ERROR debe ingresr numeros mayores a 0"
    if not(num,int):
        return "error debe ingresar numeros enteros"
    exp=0
    return contruir2(num,exp)
def contruir2(n,exp):
    if n==0:
        return exp
    elif (n%10)%2==0:
        exp=exp*10+(n%10)
        return contruir2(n//10,exp)
    elif (n%10)%2!=0:
        return contruir2(n//10,exp)
   

"""
nombre: dividirmitades
entrada, num
salida: numero dividido a la mitad
restriccion: numeros enteros
"""
def dividirmitades(num):
    if not (num,int):
        return "debe ingresar numeros enteros"
    cola=0
    return divide2(num,cola)

def divide2(num,cola):



def largo(x):
    X=x//10
    return 1





