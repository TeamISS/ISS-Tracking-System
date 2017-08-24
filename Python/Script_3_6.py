import math
import sys
import os


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
    
    nMax = 1000

    x = math.sqrt(mu)*abs(a)*dt 

    n = 0

    ratio = 1

    while (abs(ratio) > error) & (n <= nMax):
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
        

def main():
     ro = 10000
     vro = 3.0752
     dt = 3600
     a = -19655
     x = Kepler_U(dt, ro, vro, 1/a)    #1/a
     print (x)
     

if __name__ == "__main__":
    main()


