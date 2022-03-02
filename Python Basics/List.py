#sample static list
from audioop import reverse
from os import sep


thislist=['Venkat',1,1.2,'''Three''',True,"Four",{'name':'Kv'}]
print(thislist)
print('======================================================================')
#string indexing
print(thislist[0:],thislist[len(thislist)-1],thislist[-1],sep=' , ')
print('======================================================================')
#list slicing
print('Slicing output:')
print(thislist[0],thislist[::-1],thislist[2:4],sep='\n')
print('\n For Loop')
#Index Based Searching
print('1.Index Based')
for i in range(len(thislist)):
    print(thislist[i],sep=' ')
print('2.Element Based')
for i in thislist:
    print(i,sep=' ')    
ls=[]
    #append,Insert,extend
ls.append(10)
ls.extend([11,12,13]) 
ls.insert(1,22)
print('Insertion Results:',ls,sep=',')
ls=['One','Two','Three']
ls.pop(1)
print(ls)
ls1=[1,2,4,56,73,67,64,242]
ls1.sort()
print(ls1)
ls1.reverse()
print(ls1)
s='welcome'
print(len(s))
names=['Venkat','Rohit','Ramachandra raju','Sravani','Naresh']
print(sorted(names))
names.sort(key=len)
print('1.Names in increasing length')
print(names)
names.sort(key=len,reverse=True)
print('2.Names in decreasing length')
print(names)
