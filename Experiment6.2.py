import random

num = random.randint(0,100)
inp = int(input("Guess the number :"))

for i in range(6):
    if(num == inp):
        
        gussed = True
        break
    else :
        print("Remaining Chances : ",7-i-1)
        if num > inp :
            print("Actual number is higher")
        else :
            print("Acutal number is lower")
        inp = int(input("Try again :"))

if gussed:
    print('you guessed it number was',num)
else :
    print('Sorry number was',num)
