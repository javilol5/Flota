
class Tablero:
    def __init__(self, tamano):
        '''
        tamano: entero que indica filas y columnas (tablero cuadrado)
        '''
        self.dimensiones = (tamano, tamano)
        filas, columnas = self.dimensiones

        # Inicializar todas las casillas con agua (0)
        self.casillas = [[0 for _ in range(columnas)] for _ in range(filas)]

    def mostrar_tablero(self):
        """Imprime el tablero de manera legible."""
        for fila in self.casillas:
            print(" ".join(str(c) for c in fila))
        print("-" * 30)

