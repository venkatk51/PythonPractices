def getIndex(listOfIntegers,NumericVariable):
  count=0
  pos=0
  for i in range(len(listOfIntegers)):
    if listOfIntegers[i]==NumericVariable:
      count=count+1
      if count==2:
        pos=i
        break
  if pos==0:
    return 0
  else:
    return pos
if __name__ == "__main__":
  NumList=[]
  sizeList=int(input())
  for i in range(sizeList):
    NumList.append((int(input())))
  SecNum=int(input())
  res=getIndex(NumList,SecNum)
  print(res)