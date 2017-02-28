'''
Created on Feb 25, 2017

@author: thrymr
'''
a = 45  # 0010 1101
b = 28  # 0001 1100

c = a & b  #12= 0000 1100
print "Line -1 value of c is " , c
 
c = a | b # 61 = 0011 1101
print "Line -2 value of c is " , c

c = a ^ b #49 = 0011 0001
print "Line -3 value of c is " , c

a = 45
c = ~a # 210 = 1101 0010 
print "Line -4 value of c is " , c

a = 45 # 0010 1101
c = a << 2 # 180 = 1011 0100
print "Line -5 value of c is " , c

a = 45
c = a >> 2 # 0000 1011
print "Line -6 value of c is " , c 
