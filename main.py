import AGC
from maze import Maze
import numpy as np 

def imprimirSolucion(solucion):
    laberinto = Maze()
    for s in solucion:
        if s == 0:
            pass
        elif s == 1:    
            laberinto.arriba()
        elif s == 2:
            laberinto.abajo()
        elif s == 3:
            laberinto.izquierda()
        elif s == 4:
            laberinto.derecha()
    print(laberinto)
        

def main():
    s =  Maze()
    ag = AGC.AGC(64, 50 , 101, 0.5, s)
    ag.run()
    imprimirSolucion(ag._mejor_historico._cromosoma)
    


if __name__ == '__main__':
    main()
