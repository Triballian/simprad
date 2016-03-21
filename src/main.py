'''
Created on Mar 19, 2016
insprired by Curious Cheetah and Sergio
http://curiouscheetah.com/BlogMath/simplify-radicals-python-code/
http://stackoverflow.com/questions/31217274/python-simplifying-radicals-not-going-well
@author: Noe
'''

from math import modf
from math import sqrt
from os import system

#Establish input

class Sqrtinput():
   
    
    def __init__(self):
        pass
    
    

    def nsqrrt(self, a):
        answer = False
        A = a
        #check to see if the answer is an integer
        # sepsquared = squared seporated into integer and decimal parts
        squared = sqrt(A)
        fractional, integral = modf(squared)
        if fractional == 0:
            print("The answer is "+str(int(squared)))
        else:
            if A < 8:
                print 'The answer is J' + str(A)
            else:
#                print A
#Here we build a for loop ranged from 2 to spesquared[1] The devide into A .
#                 for number in range(2,int(integral)):
#may have to stake that if integral < 3 then integral +=1 may have to run a while loop here
                answer = ''
                for number in range(2,int(integral)+1):
                    print number
                    rem = A%number**2
                    if not rem:
                        answer = 'The answer is ' + str(number) + 'J' + str(A/number**2)
                        
                if not answer:
                    print('The answer is J' + str(A))
                else:                                    
                    print answer
            
                                    
    
    
    def getsqrt(self, a):
        A=a
        
        
#         A = int(raw_input("Enter the number under the radical:"))
        
        #Input taken, setup math
        B = (A + 1)
        C = sqrt(B)
        #seperate parts
        #comment added by Noe. Fractial is the fraction portion of the number Integral is the Integer
        Fractional, Integral = modf(C)
        Fractional1, Integral1 = modf(A / (Integral**2))
        def Intg(Integral):
            while Fractional == Fractional1:
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
    
    while True:
#        system('cls')
#         print('\x1b[2J')
        a = int(raw_input("Enter the number under the radical:"))
        ssqrrt = Sqrtinput()
         
    #     ssqrrt.getsqrt(a)
        ssqrrt.nsqrrt(a)
    pass
    
    
