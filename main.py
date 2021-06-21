import AGC
from laberinto import Laberinto

def imprimirSolucion(solucion):
    laberinto = Laberinto()
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
    laberinto._tablero[laberinto._actual.fila][laberinto._actual.columna] = "P"
    print("\tLaberinto final: \n")
    print(laberinto)
        

def main():
    s =  Laberinto()
    print("\tLaberinto inicial: \n")
    print(s)
    ag = AGC.AGC(100, 50, 2000, 0.5, s)
    ag.run()
    imprimirSolucion(ag._mejor_historico._cromosoma)
    

    
if __name__ == '__main__':
    main()
