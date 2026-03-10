class Nave:

    def __init__(self, nombre, tamano, vida):
        self.nombre = nombre
        self.tamano = tamano
        self.vida = vida

    def recibir_disparo(self):
        self.vida -= 1

        if self.vida > 0:
            return self.TOCADO
        else:
            return self.HUNDIDO