from ast import Num


num=int(input('Enter a number:'))
reverse_num=0
while num!=0:
    digit=num%10
    reverse_num=(reverse_num*10)+digit
    num=num//10
print(f'Reversed Number: {reverse_num}')