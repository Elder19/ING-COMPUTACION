
def factorial(num):
    if num==0:
        return 1
    else:
        return num*factorial(num-1)

def factorial2(num):
    suma=1
    return factorial4(num,suma)
def factorial4(num,suma):
    if num==0:
        return suma
    else:
        suma=suma*num
        return factorial4(num-1,suma)

def contarDigitos(num):#pila
    if num==0:
        return 0
    else:
        return 1+contarDigitos(num//10)
    
def contarDigitos2(num):#cola
    res=0
    return cont(num,res)
def cont(num,res):
    if num==0:
        return res
    else:
        res=res+1
        return cont(num//10,res)
def separarstring(string):
    cont=0
    return separarstring2(string,cont)
    
def separarstring2(string,cont):
    if string=="":
        return []
    else:
        return [string[cont]]+separarstring2(string[1:],cont=0)
    
def separarstrpila(string):
    r=[]
    return separarstrpila2(string,r)

def  separarstrpila2(string,r):
    if string=="":
        return r
    else:
        r+=[string[0]]
        return separarstrpila2(string[1:],r)
     

