import math
import sys
import os
import numpy as np


def norm(vector):

    z = 0

    for i in range(len(vector)):
        z += (vector[i]*vector[i])

    return math.sqrt(z)

def dotProduct(firstVector, secondVector):

    dot = [x*y for x,y in zip(firstVector, secondVector)]

    return sum(dot)


def coe_from_sv(R, V):

    global mu

    mu = 398600

    eps = 10**-10

    r = norm(R)

    v = norm(V)

    vr = dotProduct(R, V)/r
    
    H = np.cross(R, V)

    h = norm(H)
 
    incl = math.acos(H[2]/h)
    N = np.cross([0, 0, 1], H)

    n = norm(N)

    if n != 0:
        RA = math.acos(N[0]/n)
        if N[1] < 0:
            RA = 2*math.pi - RA
    else:
        RA = 0
        
   
    Z = 1/float(mu)
  
    E = (Z)*np.subtract((v**2 - mu/r)*np.array(R), r*vr*np.array(V))

    e = norm(E)
  
    if n != 0:
        if e > eps:
            w = math.acos(dotProduct(N, E)/n/e)
            if E[2] < 0:
                w = 2*math.pi - w
        else:
            w = 0
    else:
        w = 0

    if e > eps:
        TA = math.acos(dotProduct(E, R)/e/r)
        if vr < 0:
            TA = 2*math.pi - TA
    else:
        cp = np.cross(N, R)
        if cp[2] >= 0:
            TA = math.acos(dotProduct(N, R)/n/r)
        else:
             TA = 2*math.pi - math.acos(dotProduct(N, R)/n/r)

    a = h**2/mu/(1 - e**2)

    coe = [h, e, RA, incl, w, TA, a]
        
    return coe            
        





def main():

    global mu

    mu = 398600

    deg = math.pi/180
    
    r = [-6045, -3490, 2500]

    v = [-3.457, 6.618, 2.533]

    coe = coe_from_sv(r, v)

    if coe[1] < 1:
        T = 2*math.pi/math.sqrt(mu)*coe[6]**1.5
        
   
    
    


     
if __name__ == "__main__":
    main()
