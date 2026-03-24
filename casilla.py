class Casilla:
    """
    Representa una casilla del tablero.
    Puede contener una nave o estar vacía.
    """

    def __init__(self):
        self.nave = None       # Referencia a una nave (o None)
        self.atacada = False  # Indica si ya fue atacada

    def disparar(self):
        """
        Ejecuta un disparo sobre la casilla.
        """

        # Evitar disparos repetidos
        if self.atacada:
            print("[LOG] Ya disparaste aquí")
            return None

        # Marcar como atacada
        self.atacada = True

        # Si no hay nave → agua
        if self.nave is None:
            print("[LOG] Agua")
            return 0

        # Si hay nave → delegar daño
        resultado = self.nave.recibir_disparo()

        # Mostrar estado de la nave
        if resultado == 2:
            print(f"[LOG] {self.nave.nombre} Hundido")
        else:
            print(f"[LOG] {self.nave.nombre} Tocado ({self.nave.vida} vida restante)")

        return resultado