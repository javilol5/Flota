class Nave:
    """
    Representa una nave del juego.
    Tiene nombre, tipo y puntos de vida.
    """

    def __init__(self, nombre, tipo, vida):
        self.nombre = nombre
        self.tipo = tipo
        self.vida = vida

    def recibir_disparo(self):
        """
        Reduce la vida de la nave al recibir un disparo.
        """
        self.vida -= 1

        # Si aún tiene vida → tocado
        if self.vida > 0:
            return 1  # TOCADO

        # Si no tiene vida → hundido
        return 2  # HUNDIDO

    def __str__(self):
        """
        Representación en texto de la nave
        """
        return f"{self.nombre} ({self.tipo}) - Vida: {self.vida}"