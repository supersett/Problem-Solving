import sys

x=sys.stdin.readline().rstrip()

numA=x.count('a')
#print(numA)

listNum=[]
#print(listNum)

for k in range(len(x)):
    stringNew=x[k:numA+k]
    n=len(stringNew)
    numBefore=0
    if(len(stringNew)<numA):
      stringBefore=x[0:numA-n]
    #  print(stringBefore)
      numBefore=stringBefore.count('b')
    #print(stringNew)
    numB=stringNew.count('b')
    listNum.append(numB+numBefore)
    #print(listNum)
    

#print(listNum)
print(min(listNum))