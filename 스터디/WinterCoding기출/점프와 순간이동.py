def solution(n):
    ans = 0
    dp=[0] * (n+1)
    dp[1]=1
    for i in range(1,n+1):
        if dp[i]!=0:
          if 2*i<=n:
            dp[2*i]=dp[i]
        else:
          dp[i]=dp[i-1]+1
    ans=dp[n]
    return ans
  
#dp

