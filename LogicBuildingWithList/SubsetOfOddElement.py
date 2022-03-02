n=int(input())
list_3=[]
list_sub=[]
for i in range(n):
    list_3.append(int(input()))
for element in list_3:
    if element%2!=0:
        list_sub.append(element)    
print(list_sub)