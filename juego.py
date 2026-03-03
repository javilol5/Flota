from tablero import Tablero


class Juego:

    def __init__(self):
        self.tablero = Tablero()

    def lanzar_ataque(self, x, y):
        resultado = self.tablero.comprobar_impacto(x, y)
        self.mostrar_resultado(resultado)

    def mostrar_resultado(self, resultado):
        print("Resultado del ataque:", resultado)


if __name__ == "__main__":
    juego = Juego()
    juego.lanzar_ataque(2, 3)
    juego.lanzar_ataque(2, 3)