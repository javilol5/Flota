from tablero import Tablero
from nave import Nave


class Juego:

    def __init__(self):
        self.tablero = Tablero()

        nave = Nave("Barca", 2, 2)
        self.tablero.colocar_nave(nave)

    def lanzar_ataque(self, x, y):
        resultado = self.tablero.comprobar_impacto(x, y)
        self.mostrar_resultado(resultado)

    def mostrar_resultado(self, resultado):
        if resultado == resultado.AWA:
            print("Agua")
        elif resultado == resultado.TOCADO:
            print("Tocado")
        elif resultado == resultado.HUNDIDO:
            print("Hundido")


if __name__ == "__main__":
    juego = Juego()
    juego.lanzar_ataque(2, 3)
    juego.lanzar_ataque(2, 3)