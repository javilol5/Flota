from nave import Nave


class Tablero:

    def __init__(self):
        self.nave = Nave()

    def comprobar_impacto(self, x, y):
        return self.nave.recibir_disparo()