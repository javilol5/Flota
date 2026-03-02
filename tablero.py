
class Tablero:
    def __init__(self):


        TAMANO = 10
        self.dimensiones = (TAMANO, TAMANO)
        filas, columnas = self.dimensiones


        self.casillas = [[0 for _ in range(columnas)] for _ in range(filas)]

    def mostrar_tablero(self):

        for fila in self.casillas:
            print(" ".join(str(c) for c in fila))
        print("-" * 30)

print(Tablero.mostrar_tablero())