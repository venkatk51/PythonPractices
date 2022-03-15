salary=float(input('Enter your salary:'))
if salary>=10000:
    salary=salary + (10/100)*salary
elif salary >=6000 and salary <10000:
    salary=salary+(8/100)*salary
elif salary <6000:
    salary=salary+(5/100)*salary
print(f'Updated Salary:{round(salary,2)}')    
