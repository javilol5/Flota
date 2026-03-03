class Nave:

    def __init__(self):
        self.vida = 2

    def recibir_disparo(self):
        self.vida -= 1

        if self.vida > 0:
            return "Tocado"
        else:
            return "Hundido"