import math
import sys
import os

def Kepler_H(e, M):
    
    error = 10**-8

    F = M
        
    ratio = 1
    
    while ratio > error:
        ratio = (e*math.sinh(F) - F - M) / (e*math.cosh(F) - 1)
        F = F - ratio
   
    return F
    
    



def main():

     print (Kepler_H(2.7696, 40.69))

if __name__ == "__main__":
    main()


