import math
import sys
import os

def Kepler_E(e, M):
    
    error = 10**-8

    if M < math.pi:
        E = M + e/2
        
    else:
        E = M - e/2
        

    ratio = 1
    
    while ratio > error:
        ratio = (E - e*math.sin(E) - M) / (1 - e*math.cos(E))
        E = E - ratio
   
    return E
    
    
    



def main():

     print (Kepler_E(0.37255, 3.6029))

if __name__ == "__main__":
    main()

