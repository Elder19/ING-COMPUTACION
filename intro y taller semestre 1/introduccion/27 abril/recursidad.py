def sumarit(n):
    resultado=0
    while n!=0:
        num=n%10
        resultado+=num
        n=n//10
    return resultado


def sumarrec(n):
    if n<=9:
        return 1 
    else:
         return 1+sumarrec(n//10)

    
def tieneceros(n):
    
    if isinstance(n,int):  
        num=n%10
        if num ==0:
            return True
        else:
             num=largon(n)
             if num==1:
                 if num!=0:
                     return False
                 else:
                    return True
             else:
                 return tieneceros(n//10)    
    else:
        return "Debe ingrresar un numero entero"        
    
def largon(n):
    if n<=+9:
        return 1
    else:
        return 1+largon(n//10)

"""
nombre contarceros
salida cantidad de 0
 """

def contarceros(n):#preguntar que sea mayor a 9 si no returna 0 
    if n==0:
        return 1
    if n<0:
        n=n*-1
    else:
        if isinstance(n,int):
           
           
                num=n%10
                if num==0:
                    return 1+contarceros(n//10)
                else:
                  

                    return contarceros(n//10)


def construirpares(n):
     if n<9:
         if n%2==0:
             return n
         else:
             return 0
     if n<0:
        n=n*-1
     else:
        if isinstance(n,int):
            num=n%10
            if num%2==0:
                return construirpares(n//10)*10+num
            else:
                 return construirpares(n//10)
            
        
print(construirpares(234))