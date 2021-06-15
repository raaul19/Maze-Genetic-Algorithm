from enum import Enum
import random
from math import sqrt

class Cell(str, Enum):
    LIBRE = "-"
    BLOQUEADO = "X"
    INICIO = "I"
    META = "F"
    CAMINO = "*"

class Posicion(fila, columna):
    fila = fila
    columna = columna

class Maze:
    def __init__(self, filas, columnas, escasez):
        # initialize variables
        self._filas = filas
        self._columnas = columnas
        self._escasez = escasez
        self.inicio = Posicion(0, 0)
        self.meta = Posicion(filas - 1, columnas - 1)
        # Fill the maze
        self._tablero = [[Cell.LIBRE for c in range(columnas)] for r in range(filas)]
        # Add the BLOQUEADO cells
        self._poner_obstaculos(filas, columnas, escasez)
        self._tablero[inicio.fila][inicio.columna] = Cell.INICIO
        self._tablero[meta.fila][meta.columna] = Cell.META

    def _poner_obstaculos(self, filas, columnas, escasez):
        for fila in range(filas):
            for columna in range(columnas):
                if random.uniform(0, 1.0) < escasez:
                    self._tablero[fila][columna] = Cell.BLOQUEADO
                    
    def __str__(self):
        out = ""
        for fila in self._tablero:
            for c in fila:
                out += " "
                out += c.value
                out += " "
            out += "\n"
        return out

    def isMETACell(self, posicion):
        if posicion.fila == self.META.fila and  posicion.columna == self.meta.columna:
            return True
        return False

    def movimientos(self, posicion):
        posiciones = []
        if posicion.fila + 1 < self._filas and self._tablero[posicion.fila + 1][posicion.columna] != Cell.BLOQUEADO:
            posiciones.append(Posicion(posicion.fila + 1, posicion.columna))
        if posicion.fila - 1 >= 0 and self._tablero[posicion.fila - 1][posicion.columna] != Cell.BLOQUEADO:
            posiciones.append(Posicion(posicion.fila - 1, posicion.columna))
        if posicion.columna + 1 < self._columnas and self._tablero[posicion.fila][posicion.columna + 1] != Cell.BLOQUEADO:
            posiciones.append(Posicion(posicion.fila, posicion.columna + 1))
        if posicion.columna - 1 >= 0 and self._grid[posicion.fila][posicion.columna - 1] != Cell.BLOQUEADO:
            posiciones.append(Posicion(posicion.fila, posicion.columna - 1))
        return posiciones

    def camino(self, camino):
        for posicion in camino:
            self._tablero[posicion.fila][posicion.columna] = Cell.CAMINO
        self._tablero[self.inicio.fila][self.inicio.columna] = Cell.INICIO
        self._tablero[self.meta.fila][self.meta.columna] = Cell.META

def heuristica(meta):
    def distancia(posicion):
        x = abs(posicion.columna - meta.columna)
        y = abs(posicion.fila - meta.columna)
        return (x + y)
    return distancia