'''
Created on Mar 19, 2016
insprired by Curious Cheetah and Sergio
http://curiouscheetah.com/BlogMath/simplify-radicals-python-code/
http://stackoverflow.com/questions/31217274/python-simplifying-radicals-not-going-well
@author: Noe
'''

from math import modf
from math import sqrt
#Establish input
def sqrtinput():
    
    A = int(raw_input("Enter the number under the radical:"))
    
    #Input taken, setup math
    B = (A + 1)
    C = sqrt(B)
    #seperate parts
    Fractional, Integral = modf(C)
    Fractional1, Integral1 = modf(A / (Integral**2))
    def Intg(Integral):
        while Fractional1 == Fractional1:
            if Fractional1 == 0 and (A / (Integral**2)) == 1:
                print (Integral)
                return Integral
            else:
                Integral = (Integral - 1)
    if Integral == 1:
        print (A / (Integral**2))
    elif not Integral ==1 or (Fractional1 == 0 and (A / (Integral**2)) == 1):
        print Integral, (A / (Integral**2))
    
if __name__ == '__main__':
    sqrtinput.A()
    
    pass