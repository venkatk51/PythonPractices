import math
n=int(input())
list_4=[]
for i in range(n):
    list_4.append(int(input()))
if n%2==0:
    elements_in_single_half=n//2
    first_half=list_4[:elements_in_single_half]
    second_half=list_4[elements_in_single_half:]
    print(second_half + first_half)
else:
    middle=int(math.floor(n/2))
    first_half1=list_4[:middle]
    second_half1=list_4[middle+1:]
    print(second_half1 + [list_4[middle]]  + first_half1)


