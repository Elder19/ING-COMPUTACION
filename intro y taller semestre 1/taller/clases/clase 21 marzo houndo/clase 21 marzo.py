"""
nombre: borrar sub string
entrada: texto,texto a buscar
salida: texto sin la palabra a buscar
restricciones

"""
def borrarSubString(texto,textoabuscar):

    if(isinstance( texto,str) and(textoabuscar,str)):
        if (texto != "") and (textoabuscar !=""):
            return borrarSubString(texto,textoabuscar)


        else:
            return "error: alguno de los parametros esta vacio"
 
        return "Error debe ser un caracter de texto"





def borrarSubString(texto,textoabuscar):
    #texdelete=()
    texdelete=largotexto(textoabuscar)
    largo=largotexto(texto)
    while texto!="":
       if texto==texdelete:
           texdelete==texto[largo:]
borrarSubString("hola mundo","mu")

#CODIGOS AUX
"""
nombre: buscar en texto
entrada: texto, valor buscar 
salida: true si existe en texto
retriccion: debe ser str
"""

def buscarentextopalabras(texto,textobuscar):
    if(isinstance( texto,str) and(textobuscar,str)):
        if (texto != "") and (textobuscar !=""):
            return buscarentextopalabras_aux(texto, textobuscar)


        else:
            return "error: alguno de los parametros esta vacio"
    else:
        return "error"
def buscarentextopalabras_aux(texto, textobuscar):
    resultado= 0
    largo= largotexto(textobuscar)
    while (texto!=""):
        textoCorte = texto[0:largo]# no deberia ser l+1?
        while textobuscar== textoCorte:
            resultado+=1
            #texto=texto[1:]
        texto=texto[1:]
        
    return resultado
def largotexto(texto):
    contador=0
    for caracter in texto:
        contador+=1

    return contador
