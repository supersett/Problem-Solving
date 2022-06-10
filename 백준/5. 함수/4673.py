n=10000
def solution(n):
    N=[int(i) for i in str(n)]
    return sum(N)+n

def selfNum(n):
    content=[True]*(n+1)
    for i in range(1,n+1):
        if content[i] ==True:
            t=solution(i)
            for x in range (1,n):
                if t<n:
                    content[t]=False
                    t=solution(t)
                else:
                    break
    for i in range(1,n):
        if content[i]==True:
            print(i)
            
selfNum(n)