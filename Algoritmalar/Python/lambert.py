import sys, os, math
import numpy as np

def norm(vector):

    z = 0
    for i in range(len(vector)):
        z += (vector[i]*vector[i])           

    return math.sqrt(z)

def dotProduct(firstVector, secondVector):
        
    dot = [x*y for x,y in zip(firstVector,secondVector)]

    return sum(dot)

def lambert(R1, R2, t, string):

    global mu
    mu = 398600

    global r1, r2, A

    r1 = norm(R1)
    r2 = norm(R2)

    c12 = np.cross(R1, R2)
    theta = math.acos(dotProduct(R1,R2)/r1/r2)

    if strcmp(string, 'pro'):
        if c12[2] <= 0:
            theta = 2*math.pi - theta
    elif strcmp(string, 'retro'):
        if c12[2] >= 0:
            theta = 2*math.pi - theta
    else:
        string = 'pro'
        print ("Prograde trajectory assumed.")

   #return theta

    A = math.sin(theta)*math.sqrt(r1*r2/ (1 - math.cos(theta)))

    z = -100

    while F(z, t) < 0:
        z = z + 0.1
    #return z

    tol = 10**-8
    max = 5000

    ratio = 1
    n = 0

    while (abs(ratio) > tol)&(n <= nmax):
        n = n + 1
        ratio = F(z, t)/dFdz(z)
        z = z - ratio
    #return z

    if n >= nmax:
        print("Number of iterations exceeds")
        print("%g", nmax)

    f = 1 - y(z)/r1

    g = A*math.sqrt(y(z)/mu)

    gdot = 1 - y(z)/r2

    V1 = 1/g*(R2 - f*R1)

    V2 = 1/g*(gdot*R2 - R1)

    return V1, V2

def y(z): #dum

    global r1, r2, A
    dum = r1 + r2 + A*(z*S(z) - 1)/math.sqrt(C(z))
    return dum

def F(z, t):
    global mu, A
    dum = (y(z)/C(z))**1.5*S(z) + A*math.sqrt(y(z)) - math.sqrt(mu)*t
    return dum

def dFdz(z):
    global A
    if z == 0:
        dum = math.sqrt(2)/40*y(0)**1.5 + A/8*(math.sqrt(y(0)) + A*math.sqrt(1/2/y(0)))
    else:
        dum = (y(z)/C(z))**1.5*(1/2/z*(C(z) - 3*S(z)/2/C(z)) + 3*S(z)**2/4/C(z)) + A/8*(3*S(z)/C(z)*math.sqrt(y(z)) + A*math.sqrt(C(z)/y(z)))
    return dum

def C(z):
    dum = stumpC(z)
    return dum

def S(z):
    dum = stumpS(z)
    return dum

def main():
    global mu
    mu = 398600
    deg = math.pi/180

    r1 = [5000,10000,2100]
    r2 = [-14600,2500,7000]
    dt = 3600
    string = 'pro'

    [v1,v2] = lambert(r1, r2, dt, string)

    coe = coe_from_sv(r1, v1)

    TA1 = coe[5]

    coe = coe_from_sv(r2, v2)

    TA2 = coe[5]
    
    print(mu, r1[0], r1[1], r1[2], r2[0], r2[1], r2[2], dt, v1[0], v1[1], v2[2], v2[0], v2[1], v2[2])

    print (coe[0], coe[1], coe[3]/deg, coe[2]/deg, coe[4]/deg, TA1/deg, TA2/deg, coe[6], coe[0]**2/mu/(1 + coe[1]))

    if coe[1] < 1:
        T = 2*math.pi/math.sqrt(mu)*coe[6]**1.5
        print(T, T/60, T/3600, T/24/3600)
        
    
    

         
if __name__ == "__main__":
    main()



        
