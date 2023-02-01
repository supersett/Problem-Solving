import sys
input=sys.stdin.readline

x,y=map(int,input().split())
#24 18 
#1 2 3 4 6 8 12 24

#최대공약수 구하기(유클리드 호제법)
def cal_max(x,y):
  if x<y:
    x,y=y,x
  
  if y==0:
    return x
  else:  
    return cal_max(y,x%y)

print(cal_max(x,y))
print(x*y//cal_max(x,y))