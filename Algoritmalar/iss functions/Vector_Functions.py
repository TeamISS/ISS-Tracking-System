import sys
import os
import math
import numpy as np #pip install numpy (Python27\Script)

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

def distance(initial, satellite):

    dot = [x-y for x,y in zip(initial,satellite)]

    for i in range(len(dot)):
        dot[i] = dot[i]*dot[i]

    dist = sum(dot)                   
    return math.sqrt(dist)

def main():
       R = [-6045, -3490, 2500]
       r = norm(R)
       V = [-3.457, 6.618, 2.533]
       vr = dotProduct(R,V)/r
       mu = 398600
       v = norm(V)

       a = [2,2,2]
       b = [3,3,3]

       x = v**2-mu/r
       y = r*vr
       z = 1/float(mu)
       
       E = (z)*np.subtract((v**2-mu/r)*np.array(R), r*vr*np.array(V))
       print E
       print norm(E)
       print np.subtract(a,b)
       print "z:", z
       c=distance(a,b) 
       print c
       print math.sqrt(3)
            
         
if __name__ == "__main__":
        main()
    
