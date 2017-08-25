import sys, os, math

def J0(year, month, day):
    j0 = 367*year - fix(7*(year + fix((month + 9)/12))/4) + fix(275*month/9) + day + 1721013.5

def main():
    year = 2004
    month = 5
    day = 12

    hour = 14
    minute = 45
    second = 30

    ut = hour + minute/60 + second/3600

    j0 = J0(year, month, day)
    
    jd = j0 + ut/24
    
    print(year, month, day, hour, minute, second, jd)    
         
if __name__ == "__main__":
    main()

    
