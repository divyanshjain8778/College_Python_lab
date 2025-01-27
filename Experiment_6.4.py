#find common element between two tuples using a loop

tup1 = ("apple","banana","watermelon")
tup2 = ("watermelon","banana","orange")

for a in tup1 :
    for b in tup2:
        if a==b:
            print(a)
