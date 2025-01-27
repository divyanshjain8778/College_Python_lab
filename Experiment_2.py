import math

ax = int(input("Enter point ax : "))
ay = int(input("Enter point ax : "))
bx = int(input("Enter point bx :"))
by = int(input("Enter point by :"))


dx = ax-bx
dy = ay-by

dist = math.sqrt(dx**2 + dy**2)
print("distance between the point is :",dist)
