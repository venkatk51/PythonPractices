list_sort=[]
count=0
list_res=[]
n=int(input())
for i in range(n):
    list_sort.append(int(input()))
divi_num=int(input('Enter element for divisiblity:'))
for i in range(n):
    if list_sort[i]%divi_num==0:
        count+=1
        list_res.append(list_sort[i])
print(f'Array is {list_sort}')
print(f'{count} elements in array are divisible by {divi_num} which are {list_res}')

