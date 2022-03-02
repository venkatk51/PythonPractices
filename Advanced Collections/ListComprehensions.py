names=input().split(' ')
print(names)

'''
WAP to print sum of numbers
'''
#Traditional Approach Using For Loop

list_num=[]
num=input().split(' ')
for i in num:
    list_num.append(int(i))
num=list_num.copy()
print(sum(num))
#List Comprehension
from turtle import end_fill


numbers=input().split(" ")
numbers=[int(i) for i in numbers]
print(sum(numbers))
#dictionaries,tuples and set
# 1.Tuple ->Immutable
number1=(1,2,3,4,5)
for i in number1:
    print(i,end=' ')
# 2.Dictionaries -> {key:value}
data={
   "Name":"Venkat",
   "Age":22,
   "CT/DT No":"ABC@TCS"
}
print(data,"\n")
# 3.Set ->Collection Of Unique values
s={1,2,4,5,6}
print(s)
#given a list of duplicate data,print a list with unique values
ls=[1,1,1,1,1,2,3,3,4,5,5,5,5,5,6,6,7]
print(list(set(ls)))