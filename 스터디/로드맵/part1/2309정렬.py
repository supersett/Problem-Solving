import sys
input=sys.stdin.readline

target_9=[]
for i in range(9):
  target_9.append(int(input()))

print(target_9)
total=sum(target_9)
superbreak=False

for i in range(9):
  if superbreak==True:
    break
  for j in range(9):
    if i==j:
      continue
    a=target_9[i]
    b=target_9[j]
    if total-a-b==100:
      target_9.remove(a)
      target_9.remove(b)
      superbreak=True
      break

ans=sorted(target_9)
for i in ans:
  print(i)