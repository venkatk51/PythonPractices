list_sort=[]
n=int(input('Enter Number of Elements:'))
for i in range(n):
    list_sort.append(int(input()))
print(f'Original list:{list_sort}')
for x in range(len(list_sort)):
    for y in range(x+1,len(list_sort)):
        if list_sort[x] > list_sort[y]:
            list_sort[x],list_sort[y]=list_sort[y],list_sort[x]
print(f'Sorted List:{list_sort}')