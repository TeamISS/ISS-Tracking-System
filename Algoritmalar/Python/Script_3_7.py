import math
import sys
import os
import numpy as np

def stumpS(z):
    if z > 0:
        s = (math.sqrt(z) - math.sin(math.sqrt(z))) / (math.sqrt(z))**3
    elif z < 0:
        s = (math.sinh(math.sqrt(-z)) - math.sqrt(-z)) / (math.sqrt(-z))**3
    else:
        s = 1/6
    return s
    

def stumpC(z):
    
    if z > 0:
        c = (1 - math.cos(math.sqrt(z)))/z
    elif z < 0:
        c = (math.cosh(math.sqrt(-z)) - 1) / (-z)
    else:
        c = 1/2
    return c

def Kepler_U(dt, ro, vro, a):

    global mu

    mu = 398600

    error = 10**-8
      
    ratio = 1

    n = 0

    nMax = 1000

    x = math.sqrt(mu)*abs(a)*dt

    while (abs(ratio)>error) & (n <= nMax):
        n = n + 1
        C = stumpC(a*x**2)
        S = stumpS(a*x**2)
        F = ro*vro/math.sqrt(mu)*(x**2)*C + (1 - a*ro)*(x**3)*S + ro*x-math.sqrt(mu)*dt
        dFdx = ro*vro/math.sqrt(mu)*x*(1 - a*(x**2)*S)+(1 - a*ro)*(x**2)*C+ro
        ratio = F/dFdx
        x = x - ratio

    
    if n > nMax:
        print ("NO. Iterations of Keplers equation") #yazim hatasini d]zelt alt satira atlat
        print ("= %g" ,n)
        print ("F/dFdx = %g" , F/dFdx)
        
    return x


def f_and_g(x, t, ro, a):

    global mu

    mu = 398600

    z = a*x**2

    f = 1 - x**2/ro*stumpC(z)

    g = t - 1/math.sqrt(mu)*x**3*stumpS(z)

    return f, g

def fDot_and_gDot(x, r, ro, a):

    global mu

    mu = 398600

    z = a*x**2

    fdot = math.sqrt(mu)/r/ro*(z*stumpS(z) - 1)*x

    gdot = 1 - x**2/r*stumpC(z)

    return fdot, gdot

def norm(vector):

    z = 0

    for i in range(len(vector)):
        z += (vector[i]*vector[i])

    return math.sqrt(z)


def dotProduct(firstVector, secondVector):

    dot = [x*y for x,y in zip(firstVector, secondVector)]

    return sum(dot)


def rv_from_r0v0(R0, V0, t):

    global mu

    mu = 398600

    r0 = norm(R0)

    v0 = norm(V0)

    vr0 = dotProduct(R0, V0)/r0

    alpha = 2/r0 - v0**2/mu

    x = Kepler_U(t, r0, vr0, alpha)

    f, g = f_and_g(x, t, r0, alpha)

    R = np.multiply(f,R0) + np.multiply(g,V0)

    r = norm(R)

    fdot, gdot = fDot_and_gDot(x, r, r0, alpha)

    V = np.multiply(fdot,R0) + np.multiply(gdot,V0)

    return R, V


def main():

    global mu

    mu = 398600

    R0 = [7000,-12124,0]
    
    V0 = [2.6679,4.6210,0]

    t = 3600

    R,V = rv_from_r0v0(R0, V0, t)

    print R[1]


     
if __name__ == "__main__":
    main()
