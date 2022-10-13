

n,r,c=map(int,input().split())

cnt=0

while n!=0:
    n-=1
    size=2**n
    
    #1사분면
    if r<size and c<size:
        cnt+=0
    
    elif r<size and c>=size:
        cnt+=size*size
        c-=size
        
    elif r>=size and c<size:
        cnt+=size*size*2
        r-=size
    else:
        cnt+=size*size*3
        c-=size
        r-=size
print(cnt)