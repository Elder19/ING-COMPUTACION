def presupuestoEvento(numPersonas):
    total = 0 
    if(numPersonas > 0):
        if (numPersonas > 5) and (numPersonas < 11):
            total = numPersonas * 8500
        else:
            if (numPersonas > 10):
                total = numPersonas * 7500
            else :
                total = numPersonas * 9500
        return total
    else:
        return "Error: El número debe ser mayor a CERO"
