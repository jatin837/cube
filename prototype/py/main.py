import numpy as np
import signal
from time import sleep
import math
from math import cos, sin

## CONSTANTS & VARIABLES DECLARATIONS
DELAY: float = 1e-19
SCR_DEPTH: int = 15
CUBE_SIZE:float = 6.0
LIGHT_SRC: np.array = np.array([CUBE_SIZE + 1, CUBE_SIZE + 1, 20])
PI: float = math.pi
SCR_WIDTH: int = 60
SCR_HEIGHT: int = 28 
OFSET: np.array = np.array([SCR_WIDTH, SCR_HEIGHT, 0])
LUMINANCE:str = ".,-~:;=!*#$@"
cosD = lambda x : cos(x*PI/180) 
sinD = lambda x : sin(x*PI/180) 
O_SCR: list = [' ' for i in range(SCR_HEIGHT*SCR_WIDTH)]

## GIVEN THE SIZE OF THE CUBE, Generate a cube
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

# Every rotation i apply, will occure on origin, but translating those set of points is a better idea if you want a more robust startergy to project then onto 2D screen
def translate(v:np.array, t:np.array):
    res = v + t;
    return res 

################################################## ROTATION MATRICES ############################
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

################################################## ROTATION MATRICES(END) ########################

# Projection : THis is the most complicated part of ths whole project, how do you project 3D space onto 2D screen

def Project(v:np.array):
    global SCR_DEPTH
    global O_POINT
    x = v[0]
    y = v[1]
    z = v[2]
    k:float = 1 
    res = np.ones(2)
    res[0] = int(k*x/z)
    res[1] = int(k*y/z)
    return res

# Luminance is calculated by taking dot product of surface normal

def luminance_calc(v:np.array, O_POINT:np.array, surface_normal:np.array):
    res = np.dot(O_POINT - v, surface_normal)
    return res

# Signal handler(SIGINT) 

def handler(signum, frame):
    print("\033[1J")
    print('bye')
    exit(1)

# map the output 2D index after projection onto single array
# eg 
# 1 2 3 
# 4 5 6
# 7 8 9
# (2, 2) --> 5

def flatten(v:np.array):
    global SCR_WIDTH
    x = int(v[0])
    y = int(v[1])
    res = x + SCR_WIDTH * y
    if (res >= SCR_WIDTH*SCR_HEIGHT):
        print(f'overflow for {x}, {y} --> {res}')
    return res

## main function
if __name__ == "__main__":
    theta:float = 1.0
    r_pt = np.zeros(3)

    while True:
        print('\033[H')
        signal.signal(signal.SIGINT, handler)
        sleep(DELAY)
        cube = generate_cube(CUBE_SIZE)
        for pt in cube:
            rt_pt = translate(Rz(Ry(Rx(pt[0], theta), theta), theta), OFSET)
            p_pt:np.array = Project(r_pt)
            O_SCR[flatten(p_pt)] = '.'
            l = luminance_calc(r_pt, O_POINT, pt[1])
        for k in range(SCR_WIDTH*SCR_HEIGHT):
            if k%SCR_WIDTH == 0:
                print('\n')
            else:
                print(O_SCR[k], end = '')

        O_SCR = [' ' for i in range(SCR_HEIGHT*SCR_WIDTH)]
         
        theta += 1.0
