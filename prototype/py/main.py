import numpy as np
import signal
from time import sleep
import math
from math import cos, sin

PI: float = math.pi
cosD = lambda x : cos(x*PI/180) 
sinD = lambda x : sin(x*PI/180) 


def Rx(v:np.array, theta:float): 
    Rx_matrix:np.array  = np.array([
        [1, 0, 0],
        [0, cosD(theta), -sinD(theta)],
        [0, sinD(theta), cosD(theta)]
     ])
    res = np.matmul(Rx_matrix, v)
    return res

def Ry(v:np.array, theta:float): 
    Ry_matrix:np.array  = np.array([
        [cosD(theta), 0, sinD(theta)],
        [0, 1, 0],
        [-sinD(theta), 0, cosD(theta)]
     ])
    res = np.matmul(Ry_matrix, v)
    return res

def Rz(v:np.array, theta:float): 
    Rz_matrix:np.array  = np.array([
        [cosD(theta), -sinD(theta), 0],
        [sinD(theta), cosD(theta), 0],
        [0, 0, 1]
     ])
    res = np.matmul(Rz_matrix, v)
    return res

def Project(v:np.array):
    pass

def handler(signum, frame):
    print("\033[1J")
    print('bye')
    exit(1)
    

if __name__ == "__main__":
    v = np.array([1, 10, 0])
    while True:
        signal.signal(signal.SIGINT, handler)
        sleep(0.1)
        v = Rz(Ry(Rx(v, 34), 34), 34)
        print(v)
