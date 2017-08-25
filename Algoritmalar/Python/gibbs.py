import sys, os, math
import numpy as np
#from Vector_Functions import norm
#from Vector_Functions import dotProduct

def dotProduct(firstVector, secondVector):
        
    dot = [x*y for x,y in zip(firstVector,secondVector)]

    #d = [1,2,3,4]
    #t = [2,3,4,5]
    #dt = []                        
    #for i in range(0, len(d)):
        #dt.append(d[i]*t[i])
    return sum(dot)

def norm(vector):

    z = 0
    for i in range(len(vector)):
        z += (vector[i]*vector[i])           

    return math.sqrt(z)

def gibbs(R1, R2,R3):

    global mu
    mu = 398600
    tol = 10**-4
    ierr = 0

    r1 = norm(R1)
    r2 = norm(R2)
    r3 = norm(R3)

    c12 = np.cross(R1, R2)
    C23 = np.cross(R2, R3)
    c31 = np.cross(R3, R1)

    if abs(dotProduct(R1, c23)/r1/norm(c23)) > tol:
        ierr = 1

    N = r1*c23 + r2*c31 + r3*c12

    D = c12 + c23 + c31

    S = R1*(r2-r3) + R2*(r3-r1) + R3*(r1-r2)

    V2 = math.sqrt(mu/norm(N)/norm(D))*(np.cross(D, R2)/r2 +S)

    ##
    
def main():

    global mu

    mu = 398600.0

    deg = math.pi/180
    
    r1 = [-294.32, 4265.1, 5986.7]

    r2 = [-1365.4, 3637.6, 6346.8]

    r3 = [-2940.3, 2473.7, 6555.8]

    if ierr == 1:
        print ("These vectors are not coplanar.")
    else:
        coe = coe_from_sv(r2, v2)

        h = coe[0]
        e = coe[1]
        RA = coe[2]
        incl = coe[3]
        w = coe[4]
        TA = coe[5]
        a = coe[6]

        print("Solution:", v2[0], v2[1], v2[2], h, e, incl/deg, RA/deg, w/deg, TA/deg, a)

    if e < 1:
        T = 2*math.pi/math.sqrt(mu)*coe[6]**1.5

        print ("-------")
      


     
if __name__ == "__main__":
    main()


    


    

