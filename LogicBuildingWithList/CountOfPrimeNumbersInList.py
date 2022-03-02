from cmath import sqrt


n=int(input())
count=0
list_5=[]
for i in range(n):
    list_5.append(int(input()))
for elements in list_5:
    if elements==1 or elements==0:
        pass
    else:
        prime=True
        for num in range(2,elements):
            if elements%num==0:
                prime=False
            else:
                pass
    if prime==True:
        count+=1
print(f'There are {count} prime numbers in list') 