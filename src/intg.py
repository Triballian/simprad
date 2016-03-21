'''
Created on Mar 21, 2016
code by Sergio modified by me

@author: Noe
'''
from math import modf
from math import sqrt
#Establish input
A = int(raw_input("Enter the number under the radical:"))
#Input taken, setup math
B = (A + 1)
C = sqrt(B)
#seperate parts
Fractional, Integral = modf(C)
Integral1 = A / Integral**2
Fractional1 = A%Integral**2
answer = ''
for number in range(2,int(Integral)+1):
    print number
    rem = A%number**2
    if not rem:
        answer = 'The answer is ' + str(number) + u'\u221a' + str(A/number**2)
        
if not answer:
    print('The answer is '+ u'\u221a' + str(A))
else:                                    
    print answer

if Integral == 1:
    print (A / (Integral**2))
elif not Integral ==1 or (Fractional1 == 0 and (A / (Integral**2)) == 1):
    print 'printing Integral and A/integral square'
    print Integral