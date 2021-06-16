import AGC
from maze import Maze
import numpy as np 


def main():
    s =  Maze(10,15,0.2)
    ag = AGC.AGC(300, 50 , 1000, 0.02, s)
    
    ag.run()
    


if __name__ == '__main__':
    main()
