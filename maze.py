from enum import Enum
import random
from math import sqrt
import copy

from numpy.random import poisson

class Cell(str, Enum):
    LIBRE = "-"
    BLOQUEADO = "X"
    INICIO = "I"
    META = "F"
    CAMINO = "*"

class Posicion():
    def __init__(self, fila, columna):
        self.fila = fila
        self.columna = columna

class Maze:
    MIN_VALUE = 0
    MAX_VALUE = 1
    def __init__(self, filas, columnas, escasez):
        # initialize variables
        self._filas = filas
        self._columnas = columnas
        self._escasez = escasez
        self._inicio = Posicion(0, 0)
        self._actual = Posicion(0, 0)
        self._meta = Posicion(filas - 1, columnas - 1)
        # Fill the maze
        self._tablero = [[Cell.LIBRE for c in range(columnas)] for r in range(filas)]
        # Add the BLOQUEADO cells
        self._poner_obstaculos(filas, columnas, escasez)        
        self._tablero[self._inicio.fila][self._inicio.columna] = Cell.INICIO
        self._tablero[self._meta.fila][self._meta.columna] = Cell.META
        self._copiaTablero = copy.deepcopy(self._tablero)
        self._penalties = 0

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
        if posicion.fila == self._meta.fila and  posicion.columna == self._meta.columna:
            return True
        return False

    def mover(self, posicion):

        if self._tablero[posicion.fila][posicion.columna] == Cell.BLOQUEADO:
            self._penalties += 1
        
        if self.isMETACell(posicion) or self._tablero[posicion.fila][posicion.columna] == Cell.LIBRE:
           self._actual = posicion
           self._tablero[posicion.fila][posicion.columna] = Cell.CAMINO 
        
    def camino(self, camino):
        for posicion in camino:
            self._tablero[posicion.fila][posicion.columna] = Cell.CAMINO
        self._tablero[self._inicio.fila][self._inicio.columna] = Cell.INICIO
        self._tablero[self._meta.fila][self._meta.columna] = Cell.META

    def arriba(self):
        posicion = Posicion(self._actual.fila-1, self._actual.columna)
        if posicion.fila >= 0:
            self.mover(posicion)

    def abajo(self):
        posicion = Posicion(self._actual.fila + 1, self._actual.columna)
        if posicion.fila < self._filas:
            self.mover(posicion)

    def izquierda(self):
        posicion = Posicion(self._actual.fila, self._actual.columna-1)
        if posicion.columna >= 0:
            self.mover(posicion)

    def derecha(self):
        posicion = Posicion(self._actual.fila, self._actual.columna+1)
        if posicion.columna < self._columnas:
            self.mover(posicion)

    def fitness(self, cromosoma):
        f = 0
        for alelo in cromosoma:
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
        f = self.heuristica(self._meta, self._actual) + self._penalties
        self.reinicioTablero()
        return f

    def heuristica(self, meta, actual):
        x = abs(actual.columna - meta.columna)
        y = abs(actual.fila - meta.columna)
        return (x + y)
        

    def reinicioTablero(self):
        if self._actual != self._inicio:
            self._actual = self._inicio
        
        self._tablero = self._copiaTablero
        self._penalties = 0

