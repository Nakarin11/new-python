#Print Numeric
from math import pi
print('%.2f' %pi)
print('%.4f' %pi)
print('%.50f' %pi)
#Print String + Numeric
print('My age is', 25,'I have', 3500.50,'Bth.')
print('My age is %d, I have %.2f Bth.' %(25,3500.50))
print('My age is '+str(25)+', I have '+str(3500.50)+' Bth.')

print('5+4 =', 5+4)
print('5+4 = %.2f' %(5+4))
print('5+4 = '+str(5+4))
#Print String + String
print("I'm Nakarin", "I'll keep practicing!")
print("I'm Nakarin " + "I'll keep practicing!")
#Print Numeric + Numeric
print(1, 1, 2, 3, 5, 8, 13, 21, 34, 55)
print('%d %d %d %d %d %d %d %d %d' %(1, 1, 2, 3, 5, 8, 13, 21, 34, 55))