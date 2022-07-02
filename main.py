from typing import List
import sys
from func import *


def main(args : List[str], argc : int):
    if argc != 5:
        print("Usage: velocity_0 x_0 y_0 step")
        return -1

    velocity_0 ,x ,y ,step = float(args[1]), float(args[2]), float(args[3]), float(args[4])
    
    xs, ys = simulate_move(x,y,velocity_0, step)
    
    plot(xs,ys)
    
    return 0


if __name__ == "__main__":
    main(sys.argv, len(sys.argv))