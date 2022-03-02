word =input('Enter Word ? ')
for vowel in ['a','e','i','o','u']:
    count=0
    for letter in word:
        if letter==vowel:
            count+=1
    if count >0:
        print(f'{vowel} - {count}')  

             