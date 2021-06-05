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
O_SCR: list = [' ' for i in range(SCR_HEIGHT*SCR_WIDTH)]

def generate_cube(CUBE_SIZE:float, OFSET:np.array):

    CUBE: list = [] 
    for x in np.arange(0, CUBE_SIZE, 0.7):
        for y in np.arange(0, CUBE_SIZE, 0.7):
            z = 0
            CUBE.append([np.array([x, y, z]) + OFSET,np.array([0, 0, -1])])

    for x in np.arange(0, CUBE_SIZE, 0.7):
        for y in np.arange(0, CUBE_SIZE, 0.7):
            z = CUBE_SIZE
            CUBE.append([np.array([x, y, z]) + OFSET, np.array([0, 0, 1])])
            
    for x in np.arange(0, CUBE_SIZE, 0.7):
        for y in np.arange(0, CUBE_SIZE, 0.7):
            z = 0
            CUBE.append([np.array([x, z, y]) + OFSET, np.array([0, -1, 0])])
    for x in np.arange(0, CUBE_SIZE, 0.7):
        for y in np.arange(0, CUBE_SIZE, 0.7):
            z = CUBE_SIZE
            CUBE.append([np.array([x, z, y]) + OFSET, np.array([0, 1, 0])])
    for x in np.arange(0, CUBE_SIZE, 0.7):
        for y in np.arange(0, CUBE_SIZE, 0.7):
            z = 0
            CUBE.append([np.array([z, y, x]) + OFSET, np.array([-1, 0, 0])])
    for x in np.arange(0, CUBE_SIZE, 0.7):
        for y in np.arange(0, CUBE_SIZE, 0.7):
            z = CUBE_SIZE
            CUBE.append([np.array([z, y, x]) + OFSET, np.array([1, 0, 0])])
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
    k1:float = 10
    k2:float = 10
    x = v[0]
    y = v[1]
    z = v[2]
    res = np.ones(2)
    res[0] = k1*x/(k2 + z)
    res[1] = k1*y/(k2 + z)
    return res

def Luminance_calc(v:np.array, O_POINT:np.array, surface_normal:np.array):
    res = np.dot(O_POINT - v, surface_normal)
    return res

def handler(signum, frame):
    print("\033[1J")
    print('bye')
    exit(1)
    
def flatten(x: int, y: int){
    global SCR_WIDTH
    return x + SCR_WIDTH * y
}

if __name__ == "__main__":
    theta:float = 1.0
    r_pt = np.zeros(3)

    while True:
        signal.signal(signal.SIGINT, handler)
        sleep(0.1)
        cube = generate_cube(CUBE_SIZE, OFSET)
        print(cube)
        for pt in cube:
            r_pt = Rz(Ry(Rx(pt[0], theta), theta), theta)
            l = Luminance_calc(r_pt, O_POINT, pt[1])
            print(l)

        theta += 1.0
        print('-'*10)
