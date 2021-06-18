import AGC
from maze import Maze
import numpy as np 


def main():
    s =  Maze()
    ag = AGC.AGC(64, 100 , 10, 0.5, s)
    
    ag.run()
    


if __name__ == '__main__':
    main()
