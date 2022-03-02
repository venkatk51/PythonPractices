n=int(input())
list_1=[]
for i in range(n):
    list_1.append(int(input()))
    '''
min_element=list_1[0]
max_element=list_1[0]
for element in list_1:
    if element>max_element:
        max_element=element
    elif element<min_element:
        min_element=element
        '''

list_1.sort()
#max_element=list_1[len(list_1)-1]
#min_element=list_1[0]
print(f'Max Element:{list_1[len(list_1)-1]}')
print(f'Min Element:{list_1[0]}')

