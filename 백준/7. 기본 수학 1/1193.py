import sys
n=int(sys.stdin.readline())
t=0
for i in range(1,n+1):
    t+=i
    #해당할때
    if t>=n:
        nth=n-t+i
        #i가 짝수면 작아짐/커짐
        if i%2==0:
            oth=i-nth+1
            print(f'{nth}/{oth}')
        else:
            oth=i-nth+1
            print(f'{oth}/{nth}')
        #i가 홀수면 커짐/작아짐
        break