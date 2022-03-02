#from unicodedata import Digit


num=int(input('Enter a number:'))
sum_odd=0
sum_even=0
while num!=0:
    Digit=num%10
    if Digit%2==0:
        sum_even+=Digit
    else:
        sum_odd+=Digit
    num=num//10
print(f'Sum of even digits:{sum_even}')
print(f'Sum of odd digits:{sum_odd}')           