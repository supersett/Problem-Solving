import sys
n=int(sys.stdin.readline())

count=0

for i in range(1,n+1):
    #102
    data=list(str(i))
    #['1' '0' '2']
    if len(data)==3:
        if (int(data[1])-int(data[0]))==(int(data[2])-int(data[1])):
            count+=1
    elif len(data)==4:
        break
    else:
        count+=1
        
print(count)