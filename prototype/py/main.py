import numpy as np
import signal
from time import sleep
import math
from math import cos, sin

CUBE_SIZE:float = 6.0
O_POINT: np.array = np.array([4, 4, 9])
PI: float = math.pi
SCR_WIDTH: int = 60
SCR_HEIGHT: int = 28 
LUMINANCE:str = ".,-~:;=!*#$@"
cosD = lambda x : cos(x*PI/180) 
sinD = lambda x : sin(x*PI/180) 
O_SCR: list = [' ' for i in range(SCR_HEIGHT*SCR_WIDTH)]

def generate_cube(CUBE_SIZE:float):

    CUBE: list = [] 
    for x in np.arange(0, CUBE_SIZE, 0.7):
        for y in np.arange(0, CUBE_SIZE, 0.7):
            z = 0
            CUBE.append([np.array([x, y, z]), np.array([0, 0, -1])])

    for x in np.arange(0, CUBE_SIZE, 0.7):
        for y in np.arange(0, CUBE_SIZE, 0.7):
            z = CUBE_SIZE
            CUBE.append([np.array([x, y, z]), np.array([0, 0, 1])])
            
    for x in np.arange(0, CUBE_SIZE, 0.7):
        for y in np.arange(0, CUBE_SIZE, 0.7):
            z = 0
            CUBE.append([np.array([x, z, y]), np.array([0, -1, 0])])
    for x in np.arange(0, CUBE_SIZE, 0.7):
        for y in np.arange(0, CUBE_SIZE, 0.7):
            z = CUBE_SIZE
            CUBE.append([np.array([x, z, y]), np.array([0, 1, 0])])
    for x in np.arange(0, CUBE_SIZE, 0.7):
        for y in np.arange(0, CUBE_SIZE, 0.7):
            z = 0
            CUBE.append([np.array([z, y, x]), np.array([-1, 0, 0])])
    for x in np.arange(0, CUBE_SIZE, 0.7):
        for y in np.arange(0, CUBE_SIZE, 0.7):
            z = CUBE_SIZE
            CUBE.append([np.array([z, y, x]), np.array([1, 0, 0])])
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
    K2:int = 5
    K1:float = SCR_WIDTH*K2*3/(8*CUBE_SIZE);
    x = v[0]
    y = v[1]
    z = v[2]
    xp: int = int(SCR_WIDTH/2 + K1*z*x);
    yp: int = int(SCR_HEIGHT/2 - K1*z*y);
    res = np.ones(2)
    res[0] = int(K1*x/(K2 + z))
    res[1] = int(K1*y/(K2 + z))
    return res

def Luminance_calc(v:np.array, O_POINT:np.array, surface_normal:np.array):
    res = np.dot(O_POINT - v, surface_normal)
    return res

def handler(signum, frame):
    print("\033[1J")
    print('bye')
    exit(1)
    
def flatten(v:np.array):
    global SCR_WIDTH
    x = int(v[0])
    y = int(v[1])
    res = x + SCR_WIDTH * y
    if (res >= SCR_WIDTH*SCR_HEIGHT):
        print(f'overflow for {x}, {y} --> {res}')
    return res


if __name__ == "__main__":
    theta:float = 1.0
    r_pt = np.zeros(3)

    while True:
        print('\033[H')
        signal.signal(signal.SIGINT, handler)
        sleep(0.1)
        cube = generate_cube(CUBE_SIZE)
        for pt in cube:
            r_pt = Rz(Ry(Rx(pt[0], theta), theta), theta)
            p_pt:np.array = Project(r_pt)
            O_SCR[flatten(p_pt)] = '.'
            l = Luminance_calc(r_pt, O_POINT, pt[1])
        for k in range(SCR_WIDTH*SCR_HEIGHT):
            if k%SCR_WIDTH == 0:
                print('\n')
            else:
                print(O_SCR[k], end = '')

         
        theta += 1.0
