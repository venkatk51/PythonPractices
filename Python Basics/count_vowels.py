from calendar import c


St=input('Enter string:')
count=0
for i in St:
    if i.lower() in ['a','e','i','o','u']:
        count=count+1
        #count=count+1    
    #count=count+1
print(count)    
