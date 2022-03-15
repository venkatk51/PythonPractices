def isPalindrome(str_input):
     ls1=[]
     for i in range(len(str_input)):
        if str_input[i] in ls1:
            ls1.remove(str_input[i])
        else:
            ls1.append(str_input[i])
     if len(str_input)%2==0 and len(ls1)==0:
         return True
     elif len(str_input)%2!=0 and len(ls1)==1:
         return True
     else:
         return False

print(isPalindrome('rearcac'))
#print(isPalindrome('palindrome'))