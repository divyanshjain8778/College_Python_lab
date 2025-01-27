# write a program to demonstrating basic list operation in python
l = [2,3,45,6.8]
print(l)
print("Adding 8 to the back of the list ")
l.append(8)
print(l)
print("Removing from the back of the list")
l.pop()
print(l)
print("Updatnig value at index 2 to 12")
l[2] = 12
print(l)

'''

output :
[2, 3, 45, 6.8]
Adding 8 to the back of the list 
[2, 3, 45, 6.8, 8]
Removing from the back of the list
[2, 3, 45, 6.8]
Updatnig value at index 2 to 12
[2, 3, 12, 6.8]

'''
