import math
import sys
import os
import numpy as np


def sv_from_coe(coe):
    
    global mu
    mu = 398600
    

    h = coe[0]
    e = coe[1]
    RA = coe[2]
    incl = coe[3]
    w = coe[4]
    TA = coe[5]

    rp = np.matrix((h**2/float(mu))*(1/(1 + e*math.cos(TA))) * (math.cos(TA)*np.array([1.0, 0, 0]) + math.sin(TA)*np.array([0, 1.0, 0])))

    vp = np.matrix(mu/float(h)) * (-math.sin(TA)*np.array([1.0, 0, 0]) + (e + math.cos(TA))*np.array([0, 1.0, 0]))
    
    R3_W = np.matrix([[math.cos(RA), math.sin(RA), 0], [-math.sin(RA), math.cos(RA), 0], [0, 0, 1.0]])

    rp = rp.transpose()
    vp = vp.transpose()


    #A=transpose of R3_W

    #B=transpose of R1_i


    R1_i = np.matrix([[1.0, 0, 0], [0, math.cos(incl), math.sin(incl)], [0, -math.sin(incl), math.cos(incl)]])

    R3_w = np.matrix([[math.cos(w), math.sin(w), 0], [-math.sin(w), math.cos(w), 0], [0, 0, 1.0]])

    A = R3_W.transpose()
    B = R1_i.transpose()
    C = R3_w.transpose()

    Q_pX = A*B*C

    r = Q_pX*rp

    v = Q_pX*vp

    r = r.transpose()

    v = v.transpose()

    return r,v
        

def main():

    global mu

    mu = 398600.0

    deg = math.pi/180
    
    h = 80000.0
    e = 1.4
    RA = 40.0
    incl = 30.0
    w = 60.0
    TA =30.0

    coe = [h, e, RA*deg, incl*deg, w*deg, TA*deg]

    r,v = sv_from_coe(coe)
    

    print r , v
    
   
    
    


     
if __name__ == "__main__":
    main()
