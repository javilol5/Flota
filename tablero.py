

class Tablero:

    def __init__(self):
        self.nave = None
        self.tamano = 10

        self.AWA = 0
        self.TOCADO = 1
        self.HUNDIDO = 2

    def colocar_nave(self, nave):
        self.nave = nave

    def comprobar_impacto(self, x, y):
        if self.nave is None:
            return self.AWA
        return self.nave.recibir_disparo()