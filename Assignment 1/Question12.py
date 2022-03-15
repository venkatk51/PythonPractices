str1=input('Enter String 1:')
str2=input('Enter String 2:')
if "".join(sorted(str1))=="".join(sorted(str2)):
    print(f'{str1}=={str2} is true')
else:
    print(f'{str1}=={str2} is false')