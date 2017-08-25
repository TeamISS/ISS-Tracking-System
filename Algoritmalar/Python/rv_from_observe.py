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

def rv_from_observe(rho, rhodot, A, Adot, a, adot, theta, phi, H):
    global f, Re, wE
    deg = math.pi/180
    omega = [0,0,wE]

    A = A*deg
    Adot = Adot*deg
    a = a*deg
    adot = adot*deg
    theta = theta*deg
    phi = phi*deg

    R = np.matrix([(Re/math.sqrt(1-(2*f - f*f)*math.sin(phi)**2) + H)*math.cos(phi)*math.cos(theta), (Re/math.sqrt(1-(2*f - f*f)*math.sin(phi)**2) + H)*math.cos(phi)*math.sin(theta), (Re*(1 - f)**2/math.sqrt(1-(2*f - f*f)*math.sin(phi)**2) + H)*math.sin(phi)])
    
    Rdot = np.cross(omega, R)

    dec = math.asin(math.cos(phi)*math.cos(A)*math.cos(a) + math.sin(phi)*math.sin(a))

    h = math.acos((math.cos(phi)*math.sin(a) - math.sin(phi)*math.cos(A)*math.cos(a))/math.cos(dec))
    
    if (A > 0) & (A < math.pi):
        h = 2*math.pi - h
        return h

    RA = theta - h;

    Rho = [math.cos(RA)*math.cos(dec), math.sin(RA)*math.cos(dec), math.sin(dec)];

    r = R + rho*Rho;

    decdot = (-Adot*math.cos(phi)*math.sin(A)*math.cos(a) + adot*(math.sin(phi)*math.cos(a) - math.cos(phi)*math.cos(A)*math.sin(a)))/math.cos(dec)
    
    
    RAdot = wE + (Adot*math.cos(A)*math.cos(a) - adot*math.sin(A)*math.sin(a) + decdot*math.sin(A)*math.cos(a)*math.tan(dec)) /(math.cos(phi)*math.sin(a) - math.sin(phi)*math.cos(A)*math.cos(a))

    Rhodot = np.matrix([-RAdot*math.sin(RA)*math.cos(dec) - decdot*math.cos(RA)*math.sin(dec), RAdot*math.cos(RA)*math.cos(dec) - decdot*math.sin(RA)*math.sin(dec), decdot*math.cos(dec)])

    v = Rdot + rhodot*Rho + rho*Rhodot

def main():

    global f, Re, wE, mu
    deg = math.pi/180
    f = 1/298.256421867
    Re = 6378.13655
    wE = 7.292115e-5
    mu = 398600.4418

    rho = 2551
    rhodot = 0
    A = 90
    Adot = 0.1130
    a = 30
    adot = 0.05651
    theta = 300
    phi = 60
    H = 0

    [r,v] = rv_from_observe(rho, rhodot, A, Adot, a, adot, theta, phi, H)
    
    coe = coe_from_sv(r,v);
    h = coe[0]
    e = coe[1]
    RA = coe[2]
    incl = coe[3]
    w = coe[4]
    TA = coe[5]
    a = coe[6]
   
    rp = h**2/mu/(1 + e)

    print(rho, rhodot, A, Adot, a, adot,theta, phi, H, r(1), r(2), r(3), v(1), v(2), v(3))

    print(h, e, icl/deg, RA/deg, w/deg, TA/deg, a, rp)

    if e < 1:
        T = 2*math.pi/math.sqrt(mu)*a**1.5
        print(T, T/60, T/3600, T/24/3600)
        
     
if __name__ == "__main__":
    main()

    
        
