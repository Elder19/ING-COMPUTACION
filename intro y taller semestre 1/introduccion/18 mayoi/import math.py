import math

class rectangulo:
    def __init__(self,ancho,alto):
        self.ancho=ancho
        self.alto=alto
    def calcularea(self):
        return self.alto*self.ancho
    def calcularperimetro(self):
        return 2*(self.ancho+self.alto)
    def veraltura(self):
        return self.alto
    def verancho(self):
        return self.ancho
        
c1=rectangulo(5,6)
c1.calcularea()
