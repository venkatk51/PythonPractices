marks=int(input('Enter Marks:'))
if marks>=80:
    print(f'{marks} will grant you grade A')
elif marks>=60 and marks<80:
    print(f'{marks} will grant you grade B')
elif marks<60:
    print(f'{marks} will grant you grade C')        