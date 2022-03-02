list_sort=[]
n=int(input('Enter Number of Elements:'))
for i in range(n):
    list_sort.append(int(input()))
list_sort.sort()
if len(list_sort)>2:
    print(f'Sorted Array:{list_sort}')
    print(f'Second Largest Value in Array:{list_sort[-2]}')
else:
    print('Invalid input!')