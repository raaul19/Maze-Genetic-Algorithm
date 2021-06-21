from enum import Enum
import random

from numpy.random import poisson

class Casilla(str, Enum):
    LIBRE = "-"
    BLOQUEADO = "#"
    INICIO = "I"
    META = "F"
    CAMINO = "*"

class Posicion():
    def __init__(self, fila, columna):
        self.fila = fila
        self.columna = columna

class Laberinto:
    MIN_VALUE = 0
    MAX_VALUE = 1
    def __init__(self):
        # Inicializando variables
        self._inicio = Posicion(5, 1)
        self._actual = Posicion(5, 1)
        self._meta = Posicion(8, 13)
        self._fin = False
        self._tablero = [['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
                         ['#', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '#'],
                         ['#', '-', '#', '#', '#', '#', '-', '#', '-', '#', '#', '#', '-', '-', '#'],
                         ['#', '-', '#', '#', '#', '#', '-', '#', '-', '#', '#', '#', '-', '-', '#'],
                         ['#', '-', '#', '#', '#', '#', '#', '#', '-', '#', '-', '#', '-', '-', '#'],
                         ['#', 'I', '#', '#', '#', '#', '-', '-', '-', '#', '-', '#', '-', '-', '#'],
                         ['#', '-', '#', '#', '#', '#', '#', '#', '#', '#', '-', '#', '#', '-', '#'],
                         ['#', '-', '#', '#', '#', '-', '-', '-', '-', '-', '-', '#', '#', '-', '#'],
                         ['#', '-', '-', '-', '-', '-', '#', '#', '#', '#', '-', '-', '#', 'F', '#'],
                         ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']]    
        self._tablero[self._inicio.fila][self._inicio.columna] = Casilla.INICIO
        self._tablero[self._meta.fila][self._meta.columna] = Casilla.META
        self._sanciones = 0
                    
    def __str__(self):
        out = ""
        for fila in self._tablero:
            for c in fila:
                out += " "
                out += c
                out += " "
            out += "\n"
        return out

    def esCasillaMeta(self, posicion):
        if posicion.fila == self._meta.fila and  posicion.columna == self._meta.columna:
            return True
        return False

    def mover(self, posicion):

        if self._tablero[posicion.fila][posicion.columna] == Casilla.BLOQUEADO:
            self._sanciones += 1
        
        if self.esCasillaMeta(posicion):
            self._actual = posicion
            self._fin = True
            self._tablero[posicion.fila][posicion.columna] = "P"

        if self._tablero[posicion.fila][posicion.columna] == Casilla.LIBRE:
            self._tablero[posicion.fila][posicion.columna] = Casilla.CAMINO 
            self._actual = posicion

    def arriba(self):
        posicion = Posicion(self._actual.fila-1, self._actual.columna)
        self.mover(posicion)

    def abajo(self):
        posicion = Posicion(self._actual.fila + 1, self._actual.columna)
        self.mover(posicion)

    def izquierda(self):
        posicion = Posicion(self._actual.fila, self._actual.columna-1)
        self.mover(posicion)

    def derecha(self):
        posicion = Posicion(self._actual.fila, self._actual.columna+1)
        self.mover(posicion)

    def fitness(self, cromosoma):
        f = 0
        for alelo in cromosoma:
            if self._fin == False:
                if alelo == 0:
                    pass
                elif alelo == 1:    
                    self.arriba()
                elif alelo == 2:
                    self.abajo()
                elif alelo == 3:
                    self.izquierda()
                elif alelo == 4:
                    self.derecha()
        self._tablero[self._actual.fila][self._actual.columna] = "P"
        f = self.heuristica(self._meta, self._actual) + self._sanciones
        self.reinicioTablero()
        return f

    def heuristica(self, meta, actual):
        x = abs(meta.fila - actual.fila)
        y = abs(meta.columna - actual.columna)
        return (x + y)
        

    def reinicioTablero(self):
        if self._actual != self._inicio:
            self._actual = self._inicio
        self._tablero = [['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
                         ['#', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '#'],
                         ['#', '-', '#', '#', '#', '#', '-', '#', '-', '#', '#', '#', '-', '-', '#'],
                         ['#', '-', '#', '#', '#', '#', '-', '#', '-', '#', '#', '#', '-', '-', '#'],
                         ['#', '-', '#', '#', '#', '#', '#', '#', '-', '#', '-', '#', '-', '-', '#'],
                         ['#', 'I', '#', '#', '#', '#', '-', '-', '-', '#', '-', '#', '-', '-', '#'],
                         ['#', '-', '#', '#', '#', '#', '#', '#', '#', '#', '-', '#', '#', '-', '#'],
                         ['#', '-', '#', '#', '#', '-', '-', '-', '-', '-', '-', '#', '#', '-', '#'],
                         ['#', '-', '-', '-', '-', '-', '#', '#', '#', '#', '-', '-', '#', 'F', '#'],
                         ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']]
        self._sanciones = 0

