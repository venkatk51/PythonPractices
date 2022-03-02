userInput=int(input('Enter a Number:'))
num=1
sum=0.0
while(num<=userInput):
    fact=1
    for i in range(1,num+1):
        fact=fact*i
        i=i+1
    sum=sum+(num/fact)
    num+=1
print(f'Sum of Series is:{round(sum,3)}')