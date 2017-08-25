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

def gauss(Rho1, Rho2, Rho3, R1, R2, R3, t1, t2, t3):
    global mu
    tau1 = t1 - t2
    tau3 = t3 - t2
    tau = tau3 - tau1

    p1 = np.cross(Rho2,Rho3)
    p2 = np.cross(Rho1,Rho3)
    p3 = np.cross(Rho1,Rho2)

    Do = dotProduct(Rho1,p1)

    D = np.matrix([[dotProduct(R1,p1), dot(R1,p2), dotProduct(R1,p3)], [dotProduct(R2,p1), dotProduct(R2,p2,) dotProduct(R2,p3)],[dotProduct(R3,p1), dotProduct(R3,p2), dotProduct(R3,p3)]])

    E = dotProduct(R2,Rho2)

    A = 1/Do*(-D(1,2)*tau3/tau + D(2,2) + D(3,2)*tau1/tau)
    B = 1/6/Do*(D(1,2)*(tau3**2 - tau**2)*tau3/tau + D(3,2)*(tau**2 - tau**2)*tau1/tau)

    a = -(A**2 + 2*A*E + norm(R2)**2)
    b = -2*mu*B*(A + E)
    c = -(mu*B)**2

    Roots = roots([1, 0, a, 0, 0, b, 0, 0, c])

    x = posroot(Roots)

    f1 = 1 - 1/2*mu*tau1**2/x**3
    f3 = 1 - 1/2*mu*tau3**2/x**3

    g1 = tau1 - 1/6*mu*(tau1/x)**3
    g3 = tau3 - 1/6*mu*(tau3/x)**3

    rho2 = A + mu*B/x**3

    rho1 = 1/Do*((6*(D(3,1)*tau1/tau3 + D(2,1)*tau/tau3)*x**3 + mu*D(3,1)*(tau**2 - tau1**2)*tau1/tau3) /(6*x**3 + mu*(tau**2 - tau3**2)) - D(1,1))

    rho3 = 1/Do*((6*(D(1,3)*tau3/tau1 - D(2,3)*tau/tau1)*x**3 + mu*D(1,3)*(tau**2 - tau3**2)*tau3/tau1) /(6*x**3 + mu*(tau**2 - tau3**2)) - D(3,3))

    r1 = R1 + rho1*Rho1
    r2 = R2 + rho2*Rho2
    r3 = R3 + rho3*Rho3

    v2 = (-f3*r1 + f1*r3)/(f1*g3 - f3*g1)

    r_old = r2
    v_old = v2

    rho1_old = rho1
    rho2_old = rho2
    rho3_old = rho3
    diff1 = 1
    diff2 = 1
    diff3 = 1
    n =0
    nmax = 1000
    tol = 10**-8

    while ((diff1 > tol) & (diff2 > tol) & (diff3 > tol)) & (n < nmax):
        n = n+1;

    ro = norm(r2)
    vo = norm(v2)
    vro = dotProduct(v2,r2)/ro
    a = 2/ro - vo**2/mu

    x1 = kepler_U(tau1, ro, vro, a)
    x3 = kepler_U(tau3, ro, vro, a)

    [ff1, gg1] = f_and_g(x1, tau1, ro, a)
    [ff3, gg3] = f_and_g(x3, tau3, ro, a)

    f1 = (f1 + ff1)/2
    f3 = (f3 + ff3)/2
    g1 = (g1 + gg1)/2
    g3 = (g3 + gg3)/2

    c1 = g3/(f1*g3 - f3*g1)
    c3 = -g1/(f1*g3 - f3*g1)

    rho1 = 1/Do*( -D(1,1) + 1/c1*D(2,1) - c3/c1*D(3,1))
    rho2 = 1/Do*( -c1*D(1,2) + D(2,2) - c3*D(3,2))
    rho3 = 1/Do*(-c1/c3*D(1,3) + 1/c3*D(2,3) - D(3,3))

    r1 = R1 + rho1*Rho1
    r2 = R2 + rho2*Rho2
    r3 = R3 + rho3*Rho3

    v2 = (-f3*r1 + f1*r3)/(f1*g3 - f3*g1)

    diff1 = abs(rho1 - rho1_old)
    diff2 = abs(rho2 - rho2_old)
    diff3 = abs(rho3 - rho3_old)

    rho1_old = rho1
    rho2_old = rho2
    rho3_old = rho3

    print(n)

    if n >= nmax:
        print(nmax)

    r = r2
    v = v2
    return r2, v2

def posroot(Roots):
    posroots = Roots(find(Roots>0 & ˜imag(Roots)))
    npositive = length(posroots)

    if npositive == 0:
        print("There are no positive roots.")
    if npositive == 1:
        x = posroots
    else:
        print("There are two or more positive roots.")
        for i = 1:npositive:
            print('\n root #%g = %g', i, posroots(i))

        fprintf('\n\n Make a choice:\n')
        nchoice = 0
    while nchoice < 1 | nchoice > npositive:
        nchoice = input(' Use root #? ')

    x = posroots(nchoice)
    print(x)


def main():

    global mu
    deg = math.pi/180
    mu = 398600
    Re = 6378
    f = 1/298.26

    H =1
    phi = 40*deg
    t = [ 0 118.104 237.577]
    ra = [43.5365, 54.4196, 64.3178]*deg
    dec = [-8.78334, -12.0739, -15.1054]*deg
    theta = [44.5065, 45.000, 45.4992]*deg

    fac1 = Re/math.sqrt(1-(2*f - f*f)*math.sin(phi)**2)
    fac2 = (Re*(1-f)**2/math.sqrt(1-(2*f - f*f)*math.sin(phi)**2) + H) *math.sin(phi)
    for i = 1:3:
        R[i,1] = (fac1 + H)*math.cos(phi)*math.cos(theta(i))
        R[i,2] = (fac1 + H)*math.cos(phi)*math.sin(theta(i))
        R[i,3] = fac2
        rho[i,1] = math.cos(dec(i))*math.cos(ra(i))
        rho[i,2] = math.cos(dec(i))*math.sin(ra(i))
        rho[i,3] = math.sin(dec(i))

    [r, v, r_old, v_old] = gauss(rho(1,:), rho(2,:), rho(3,:), R(1,:), R(2,:), R(3,:), t(1), t(2), t(3))

    print (gauss)


     
if __name__ == "__main__":
    main()
    
    
    

