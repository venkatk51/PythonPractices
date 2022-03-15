x=int(input('Enter Number:'))
reverse=0
temp=x
while x>0:
    digits=x%10
    reverse=(reverse*10)+digits
    x=x//10
if temp==reverse:
    print(True)
else:
    print(False)
'''
num=int(input("Enter a number:"))
temp=num
rev=0
while(num>0):
    dig=num%10
    rev=rev*10+dig
    num=num//10
if(temp==rev):
    print(True)
else:
    print(False)
'''