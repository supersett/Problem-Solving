import sys
sys.setrecursionlimit(10000)
n=int(sys.stdin.readline().rstrip())

dp=[0 for i in range(n+1)]


def cal(x):
    if x==1:
        dp[1]=1
        return 1
    elif x==2:
        dp[2]=2
        return 2
    elif x==3:
        dp[3]=3
        return 3
    elif dp[x]!=0:
        return dp[x]
    else:
        dp[x]=cal(x-1)+(cal(x-2))
        return dp[x]
      
print(cal(n)%10007)
      