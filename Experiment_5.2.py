    
inp = input("Enter the number :")
n = len(inp)
num = int(inp)
temp = num
res = 0
while temp!=0 :
    rem = temp%10
    temp//=10
    res += rem**n

if res == num:
    print("Yes the num",num,"is armstrong")
else :
    print("Number",num," is not a armstrong")
