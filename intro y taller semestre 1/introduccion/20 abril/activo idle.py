def sumamatriz(matriz,matrizz):
    s=0
    nuevam=[]
    m=0
    contador=0
    largo2=largol(matriz)
    largo1=largol(matrizz)
    while m<=largo2:

        if largo2==largo1:
            x=matriz[contador]
            a=matrizz[contador]
            tamaño1=largol(x)
            tamaño2=largol(a)

            if  tamaño1== tamaño2:
                nuevam+=(a[s]+x[s])
                s+=1
                    
            if contador==tamaño1:
                matriz+=[nuevam]
                nuevam=[]
                contador=0
                m+=1
                print(matriz)
        else:
            return "Error la matriz nocumple con el mismo tamaño"
            

  

def largol(x):
    contador=0
    for elemento in x:
        contador+=1
    return contador
print(sumamatriz([[0,1],[0,2]],[[0,1],[0,2]]))
