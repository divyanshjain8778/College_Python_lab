
#Find the largest product of numbers in list 
import math
l = [2,3,4,8,9,2,11]

max_prod = 0

for i in range(0,len(l)):
    for j in range(i+1,len(l)):
        max_prod = max(max_prod, l[i] * l[j])


print("larget product of number in list is :",max_prod)


'''
output : 
larget product of number in list is : 99
'''
