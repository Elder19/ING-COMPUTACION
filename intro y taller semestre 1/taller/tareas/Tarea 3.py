import tkinter as tk
from tkinter import *
from tkinter import messagebox as mb
ventana=Tk()
ventana.title="Calculadora"
ventana.geometry("300x250")
ventana.config(bg="gray44")
ventana.resizable(False, False)  # evitar que la ventana se pueda expandir

# formar los numero~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def formaN(n):
    global operador
    operador=operador+str(n)
    input_text.set(operador)

# limpiar pantalla ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def LimpiarPantalla():
    global operador
    operador=""
    input_text.set("0")

# de decimal a binario ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def binario():
    global operador
    try:
        operador0=int(operador)
    except:
        operador=""
        input_text.set("0")
        mb.showerror("Cuidado","para hacer la convercion a binarios solo deben haber numeros")
    if operador0 <=0:
        operador=""
        input_text.set("0")
        mb.showerror("Cuidado","el numero debe ser mayor a 0")
    total=0
    contador=0
    x=0
    while operador0!=0:
        x=operador0%2
        operador0//=2
        total+=x*10**contador
        contador+=1
    total=str(total)
    operador=total
    input_text.set(operador)


# de binario a decimal ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def decimal():
    global operador
    try:
        operador0=int(operador)
    except:
        operador=""
        input_text.set("0")
        mb.showerror("Cuidado","para hacer la convercion a decimal solo deben haber numeros")

    for elemento in operador:
        num=int(elemento)
        if num >=0 and num<=1:
            continue
        else:
            operador=""
            input_text.set("0")
            mb.showerror("Cuidado","para hacer la convercion a binarios solo deben haber 0 y 1")
    total=0
    contador=largonum(operador0)
    while contador>=0:
        x=operador0%10
        total+=x*2**contador
        contador-=1
        operador0//=10
    total=str(total)
    operador=total
    input_text.set(operador)


def largonum(num):
    contador=0
    while num !=0:
        num//=10
        contador +=1
    contador-=1
    return contador


#OPERACIONBASICA~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def final():
     
    global operador
  
    cont=-1
    num=0
    n1=0
    lista=[]
    total=0
    
    for caracter in operador:
        elemento=caracter
        
        try:

            num=num*10+int(elemento)
        except:
            lista+=[num]
            num=0
            lista+=[elemento]
    largo=long(lista)
    lista+=[num]
  
    if largo<=3:
        x=opereacioncombina(lista)
        x=str(x)
        operador=x
        input_text.set(operador)
    else:
         operador=""
         input_text.set("0")
         mb.showerror("Cuidado","La calculadora solo recibe dos numeros")
    

def opereacioncombina(x):
    lista=[0,0,0]
    lista=x 
    total=lista[0]
 

    final=0
    for elemento in lista:
        
        if lista!=[]:
       
            if lista[1]=="+":
                
                total+=lista[2]
                L=long(lista)
                
                lista=[]
               
                  
            elif lista[1]=="-":
                total-=lista[2]
                L=long(lista)
                if  L<=3:
                    lista=[]
                else:
                    lista=lista[2:]
                 

            elif lista[1]=="*":
                total=total*lista[2]
                L=long(lista)
                if  L<=3:
                    lista=[]
                else:
                    lista=lista[2:]
            elif lista[1]=="/":
                total/=lista[2]
                L=long(lista)
                if L<=3:
                    lista=[]
                else:
                    lista=lista[2:]
                   
           
                   
            elif lista[1]=="D":
                total//=lista[2]
                L=long(lista)
                if L<=3:
                    lista=[]
                else:
                    lista=lista[2:]
                   
                    
            elif lista[1]=="P":
                total**=lista[2]
                L=long(lista)
                if  L<=3:
                    lista=[]
                else:
                    lista=lista[2:]
            elif lista[1]=="%":
                total%=lista[2]
                L=long(lista)
                if  L<=3:
                    lista=[]
                else:
                    lista=lista[2:]
              
                

            else:
                final=1
            
        
        return(total)

    
def long(num):
    x=0
    for elemento in num:
        x+=1
    return x





# fibonacci~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def fibonacci():
    global operador
    try:
        operador0=int(operador)
    except:
        operador=""
        input_text.set("0")
        mb.showerror("Cuidado","para hacer realizar el fibonacci solo deben haber numeros")
    if operador0 <=0:
        operador=""
        input_text.set("0")
        mb.showerror("Cuidado","para hacer realizar el fibonacci el numero debe ser mayor a 0")
    if operador0>30:
        operador="" 
        input_text.set("0")
        mb.showerror("Cuidado","para evitar sobrecarga el numero debe ser menor a 30")
    operador0= fibonacciAUX(operador0)
    operador0=str(operador0)
    operador=operador0
    input_text.set(operador)

def fibonacciAUX(n):
    if n == 1:
        return 1
    elif n==0:
        return 0
    else:
        return fibonacciAUX(n-1) + fibonacciAUX(n-2)

#factorial~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def factorial():
    global operador
    try:
        num=int(operador)
    except:
        operador=""
        input_text.set("0")
        mb.showerror("Cuidado","para hacer realizar el fibonacci solo deben haber numeros")
    if num == 0:
        return 0
    else:
        num=aux(num,1)
        operador=str(num)
        input_text.set(operador)
    
def aux(num,total):
    if num==1:
        return total*1
    else:
        total*=(num)
        return aux(num-1,total)




operador=""
input_text=StringVar()#que hace 
resultado=Entry(ventana,textvariable=input_text)


#teclado:~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


N0=Button(ventana,text="0",command=lambda:formaN(0))
N1=Button(ventana,text="1",command=lambda:formaN(1))
N2=Button(ventana,text="2",command=lambda:formaN(2))
N3=Button(ventana,text="3",command=lambda:formaN(3))
N4=Button(ventana,text="4",command=lambda:formaN(4))
N5=Button(ventana,text="5",command=lambda:formaN(5))
N6=Button(ventana,text="6",command=lambda:formaN(6))
N7=Button(ventana,text="7",command=lambda:formaN(7))
N8=Button(ventana,text="8",command=lambda:formaN(8))
N9=Button(ventana,text="9",command=lambda:formaN(9))
punto=Button(ventana,text=".",command=lambda:formaN("."))
total=Button(ventana,text="=",command=final)
bi=Button(ventana,text="binario",command=binario)
limpiar=Button(ventana,text="C",command=LimpiarPantalla)
decimal=Button(ventana,text="decimal",command=decimal)
fibonacci=Button(ventana,text="fibonacci",command=fibonacci)
suma=Button(ventana,text="+",bg="bisque3",command=lambda:formaN("+"))
Resta=Button(ventana,text="-",bg="bisque3",command=lambda:formaN("-"))
multiplicar=Button(ventana,text="x",bg="bisque3",command=lambda:formaN("*"))
dividir=Button(ventana,text="%",bg="bisque3",command=lambda:formaN("%"))
divi=Button(ventana,text="//",bg="bisque3",command=lambda:formaN("D"))
potencia=Button(ventana,text="**",bg="bisque3",command=lambda:formaN("P"))
factorial=Button(ventana,text="factorial",command=factorial)




# ubicacion de teclas~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
N9.place(x=150,y=110,width=50,height=30)
N8.place(x=100,y=110,width=50,height=30)
N7.place(x=50,y=110,width=50,height=30)

N6.place(x=150,y=80,width=50,height=30)
N5.place(x=100,y=80,width=50,height=30)

N4.place(x=50,y=80,width=50,height=30)
N3.place(x=150,y=50,width=50,height=30)
N2.place(x=100,y=50,width=50,height=30)
N1.place(x=50,y=50,width=50,height=30)
N0.place(x=50,y=140,width=50,height=30)

punto.place(x=100,y=140,width=50,height=30)
total.place(x=150,y=140,width=50,height=30)
limpiar.place(x=50,y=170,width=50,height=30)
bi.place(x=100,y=170,width=50,height=30)
decimal.place(x=150,y=170,width=50,height=30)
fibonacci.place(x=50,y=200,width=75,height=30)
factorial.place(x=125,y=200,width=75,height=30)

suma.place(x=220,y=50,width=50,height=30)
Resta.place(x=220,y=80,width=50,height=30)
multiplicar.place(x=220,y=110,width=50,height=30)
dividir.place(x=220,y=140,width=50,height=30)
divi.place(x=220,y=170,width=50,height=30)
potencia.place(x=220,y=200,width=50,height=30)
resultado.place(x=50,y=10,width=150,height=30)

ventana.mainloop()
