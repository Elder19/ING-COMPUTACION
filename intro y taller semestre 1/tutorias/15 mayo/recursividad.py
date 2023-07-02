def contarceros(x):
    
    if isinstance (x,list):
        long=largo(x)
        
        return cortax(x,0,long)
def cortax(num,indice,long):
    if indice==long:
        return 0
    else:
        return aux(num,num[indice],indice,long,0)  
def aux(num,numero,indice,long):
    
    if numero==[]:
        return cortax(num,indice+1,long)
    
    if numero[0]==0: 
        numero=numero[1:]
        return  aux(num,numero,indice,long)+1
        
    else:
         numero=numero[1:]
         return  aux(num,numero,indice,long)
              
        
def largo(x):
    if x==[]:
        return 0
    else:
        return largo(x[1:])+1  
    
print(contarceros([[0,0,0,0],[8,8,0,5],[5,5,0]]))


