#from csv import list_dialects
def countInRange(x,y,list_sort,list_size):
    count=0
    for i in range(list_size):
        if(list_sort[i]>=x and list_sort[i]<=y):
            count+=1
    return count
list_sort=[]
n=int(input('Enter Number of Elements:'))
for i in range(n):
    list_sort.append(int(input()))
start_range=int(input('Enter range start point:'))
end_range=int(input('Enter range end point:'))
list_size=len(list_sort)
res=countInRange(start_range,end_range,list_sort,list_size)
if res!=0:
    print(f'Values between {start_range} and {end_range} is {res}')
else:
    print('No Values found')    
