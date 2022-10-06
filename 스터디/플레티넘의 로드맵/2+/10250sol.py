t=int(input())
 
for _ in range(t):
    h,w,n=map(int,input().split())
    
    y = n % h
    x = (n//h)+1
    
    #나머지가 0인 경우 문제 생김
    if y==0:    
        y=h
        x=x-1
    print(y*100+x)