def num(m, n, x, y):
    while x <= m * n:
        if (x - y) % n == 0:
            return x
        x += m
    return -1

t = int(input())
for i in range(t):
    m, n, x, y = map(int, input().split())
    print(num(m, n, x, y))
    
# 간단한 규칙을 찾아보자. k번째 해 즉, 정답을 k라고 하자.

 

# k - x에 m을 나누면 나머지가 0이다.

 

# 마찬가지로 k - y에 n을 나누면 나머지가 0이다.

 

# 정답 k는 x나 y에 m과 n을 계속 더한 값중 하나다.

 

# x에 m을 계속 더해주고 y를 뺀값에 n이 나누어 떨어진다면 그 값이 정답이다.