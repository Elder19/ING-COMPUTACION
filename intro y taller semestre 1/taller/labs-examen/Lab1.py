
def areaTrapecio(B, b, h):
    if B>0 and b>0 and h>0:
        return (B + b) * h / 2 #area de trapecio


def grupoPoblacion(edad):
    if edad>=0 and edad<=125:
        if edad>0 and edad<=10:
            return "Niños"
        elif edad>10 and edad<=18:
            return "Adolecentes"
        elif edad>18 and edad<=50:
            return "Adultos"
        elif edad>50 and edad<=125:
            return "ancianos"
        elif edad>125:
            return "Es una edad poco probable, favor consultar"
    else:
        return "negativo devolver el mensaje respectivo a valores entre 0 a 125"
    

    
def sonImpares(num):
    dig=0
    if isinstance (num,int)and num>=0:
        dig=0
        while num!=0:
            dig= num % 10 # quite el ultimo numero de num
            num=num//10 # agarra el ultimo numero
            if dig % 2 ==0:
                return False
        return True
