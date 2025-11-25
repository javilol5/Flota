from Flota import Barco
from Flota import Tablero

if __name__ == "__main__":
    submarino = Barco("Submarino", 1)
    submarino.mostrar_estado()

    submarino.recibir_impacto()
    submarino.mostrar_estado()
    print("¿Está hundido el Submarino?", submarino.esta_hundido())

    buque = Barco("Buque", 3)
    buque.mostrar_estado()

    buque.recibir_impacto()
    buque.recibir_impacto()
    buque.mostrar_estado()
    print("¿Está hundido el Buque?", buque.esta_hundido())

    buque.recibir_impacto()
    buque.mostrar_estado()
    print("¿Está hundido el Buque ahora?", buque.esta_hundido())

    if __name__ == "__main__":
        tablero = Tablero(5)
        print("Tablero 5x5 inicializado con agua:")
        tablero.mostrar_tablero()