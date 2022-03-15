from secrets import choice


int_a=int(input('Enter int a:'))
int_b=int(input('Enter int b:'))
print('<========= WELCOME TO CALCULATOR ============>')
print('Enter your choice:')
choices=int(input())
if choices==1:
    print(f'{int_a} + {int_b} = {int_a + int_b}')
elif choices==2:
    print(f'{int_a} - {int_b} = {int_a - int_b}')
elif choices==3:
    print(f'{int_a} ^ {int_b} = {int_a ** int_b}')
elif choices==4:
    print(f'{int_a} * {int_b} = {int_a * int_b}')
else:
    print('Invalid choice Exiting Application!!')
print('<===============================================>')