count=int(input('Enter Count:'))
Min,Max,sum,count1=count,0,0,0
print('Enter Numbers:')
while count1<count:
    num=int(input())
    count1+=1
    if num<Min:
        Min=num
    elif num>Max:
        Max=num
    sum=sum+num
print(f'Average:{(sum/count)}')
print(f'Largest Num:{Max}')
print(f'Smallest Num:{Min}')       
