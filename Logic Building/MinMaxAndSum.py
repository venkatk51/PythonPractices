num=int(input('Enter a number:'))
temp=num
largest_num,smallest_num,sum=0,0,0
while temp!=0:
    digit=temp%10
    if largest_num<digit:
        largest_num=digit
    else:
        smallest_num=digit
    sum=sum+digit
    temp=temp//10
print(f'Largest digit:{largest_num}')
print(f'Smallest digit:{smallest_num}')
print(f'Sum:{sum}')


