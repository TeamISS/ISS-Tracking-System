import sys
import os
import math
import numpy as np

def julianDate(year,month,day):

    if int(month) == 1 | int(month) == 2:
        year = year-1
        month = month + 12
    else:    
        A = int(int(year)/100)
        B = 2-A+int(A/4)
        C = int(365.25*int(year))
        E = int(30.6001*(int(month)+1))

        JD = B + C + int(day) + E + 1720994.5
        
        return JD

def greenwichSidereal(juliandate):

    JD = juliandate
    T = (JD-2451545.0)/36525.0
    UT = 4.5
    T0 = 6.697374558+ (2400.051336*T)+(0.000025862*T**2)+(UT*1.0027379093)
    while T0 >  0:
        T0 = T0 - 24

    if T0 < 0:
        T0 = T0 + 24

    return T0

def localSiderealtime():
    
    year = raw_input("To calculate JulianDate, Enter year ")
    month = raw_input("Enter month ")
    day = raw_input("Enter day ")
    juliandate = julianDate(year,month,day)
    GST = greenwichSidereal(juliandate)
    L = float(input("Enter east longitude"))
    LST = GST + (L/15)
    
    while LST > 0:
        LST = LST -24
        
    if LST< 0:
        LST = LST + 24

    radLST = 7.27 * 10**-5 * 3600 * LST

    return radLST
        

def main():
    
   print localSiderealtime()
   
            
      
if __name__ == "__main__":
        main()
        
   
    

