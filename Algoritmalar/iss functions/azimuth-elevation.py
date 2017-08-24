import sys
import os
import math
import numpy as np
from Vector_Functions import norm, distance


def oldrangeVector(satellite, initial):
    
    r = [x-y for x,y in zip(satellite, initial)]
    return r

def newrangeVector():

    satellite = [3220.788, 3268.788, 4983.089]
    biz = [4126.088, 2659.977, 4059.869]
    vector = oldrangeVector(satellite,biz)

    rx = vector[0]
    ry = vector[1]
    rz = vector[2]

    sideReal = math.radians(228.55)

    rS = math.sin(sideReal)*math.cos(0.694)*rx + math.sin(sideReal)*math.sin(0.694)*ry - math.cos(sideReal)*rz

    rE = -math.sin(0.694)*rx + math.cos(0.694)*ry

    rZ = math.cos(sideReal)*math.cos(0.694)*rx + math.cos(sideReal)*math.sin(0.694)*ry + math.sin(sideReal)*rz

    newr = [rS, rE, rZ]
    
    return newr

def azimuth(vector):

    Az = math.atan(-vector[1]/vector[0])

    return math.degrees(Az)

def elevation(vector):

    r = norm(vector)

    el = math.asin(vector[2] / r)

    return math.degrees(el)
    


def main():
    satellite = [3220.788, 3268.788, 4983.089]
    biz = [4126.088, 2659.977, 4059.869]
    a = newrangeVector()
    b =oldrangeVector(satellite, biz)

    print norm(a), a , "Azimuth:", azimuth(a), "Elevation:" , elevation(a)
    print norm(b), b , "Azimuth:", azimuth(b), "Elevation:" , elevation(b)
    
            
         
if __name__ == "__main__":
        main()
