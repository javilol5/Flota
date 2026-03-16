from tablero import Tablero
from nave import Nave


class Juego:

    def __init__(self):
        pass


    def inicializar_naves(self):
        pass

    def lanzar_ataque(self, x, y):
        print(f"Atacando a  {x}, {y} ")
        obj_tablero = Tablero()
        resultado = obj_tablero.comprobar_impacto(x, y)
        self.mostrar_resultado(resultado)

    def mostrar_resultado(self, resultado):
        if resultado == 0:
            print("Awa")
        elif resultado == 1:
            print("Tocado")
        elif resultado == 2:
            print("Hundido")


if __name__ == "__main__":
    juego = Juego()
    juego.lanzar_ataque(2, 3)
    juego.lanzar_ataque(2, 3)
    juego.lanzar_ataque(1, 1)
    juego.lanzar_ataque(4, 0)
    juego.lanzar_ataque(7, 6)