list_sort=[]
flag=0
n=int(input('Enter Number of Elements:'))
for i in range(n):
    list_sort.append(input())
search_element=input('Enter Element to searched:')
for i in list_sort:
    if i==search_element:
        flag=flag+1
if (str(search_element).isdigit()):
    print(f'{search_element} is numeric ')
else:
    print(f'{search_element} is a string')
if flag!=0:
    print(f'Yes! {search_element} exists in list {list_sort}')
else:
    print(f'No! {search_element} does not contains in list {list_sort}')    



