n=int(input())
list_2=[]
sum=0
for i in range(n):
    list_2.append(int(input()))
for element in list_2:
    sum=sum+element
print(f'Average of all elements:{sum/n}')

