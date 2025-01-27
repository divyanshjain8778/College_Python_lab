
inp = input("Enter the number :") 
isPalindrome = True
for i in range(len(inp)//2):
    if inp[i]!=inp[len(inp)-i-1]:
        isPalindrome = False
        break
if isPalindrome :
    print("it is a palindrome")
else :
    print("its not a palindrome")
    
