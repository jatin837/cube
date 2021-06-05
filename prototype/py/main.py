import numpy as np
import signal
from time import sleep
import math
from math import cos, sin

CUBE_SIZE:float = 6.0
OFSET:np.array = np.array([CUBE_SIZE/2+4, CUBE_SIZE/2 + 4, 0 ])
O_POINT: np.array = np.array([OFSET[0], OFSET[1], 12])
PI: float = math.pi
SCR_WIDTH: int = 60
SCR_HEIGHT: int = 24 
LUMINANCE:str = ".,-~:;=!*#$@"
cosD = lambda x : cos(x*PI/180) 
sinD = lambda x : sin(x*PI/180) 

def generate_cube(CUBE_SIZE:float, OFSET:np.array):

    CUBE: list = [] 
    for x in np.arange(0, CUBE_SIZE, 0.7):
        for y in np.arange(0, CUBE_SIZE, 0.7):
            z = 0
            CUBE.append(np.array([x, y, z]) + OFSET)
            print(CUBE)

    for x in np.arange(0, CUBE_SIZE, 0.7):
        for y in np.arange(0, CUBE_SIZE, 0.7):
            z = CUBE_SIZE
            CUBE.append(np.array([x, y, z]) + OFSET)
            
    for x in np.arange(0, CUBE_SIZE, 0.7):
        for y in np.arange(0, CUBE_SIZE, 0.7):
            z = 0
            CUBE.append(np.array([x, z, y]) + OFSET)
    for x in np.arange(0, CUBE_SIZE, 0.7):
        for y in np.arange(0, CUBE_SIZE, 0.7):
            z = CUBE_SIZE
            CUBE.append(np.array([x, z, y]) + OFSET)
    for x in np.arange(0, CUBE_SIZE, 0.7):
        for y in np.arange(0, CUBE_SIZE, 0.7):
            z = 0
            CUBE.append(np.array([z, y, x]) + OFSET)
    for x in np.arange(0, CUBE_SIZE, 0.7):
        for y in np.arange(0, CUBE_SIZE, 0.7):
            z = CUBE_SIZE
            CUBE.append(np.array([z, y, x]) + OFSET)
    print(CUBE)
    return np.array(CUBE)


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
    # What should the projection logic?
    pass

def Luminance_calc(v:np.array, O_POINT:np.array, surface_normal:np.array):
    res = np.dot(O_POINT - v, surface_normal)
    return res

def handler(signum, frame):
    print("\033[1J")
    print('bye')
    exit(1)
    

if __name__ == "__main__":
    theta:float = 1.0
    r_pt = np.zeros(3)

    while True:
        signal.signal(signal.SIGINT, handler)
        sleep(0.1)
        cube = generate_cube(CUBE_SIZE, OFSET)
        print(cube)
        for pt in cube:
            r_pt = Rz(Ry(Rx(pt, theta), theta), theta)
            print(r_pt, end = ' ')

        theta += 1.0
        print('-'*10)
