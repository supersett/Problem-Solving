import sys

target_list=[]

while True:
    n =sys.stdin.readline().rstrip()
    if n=='0':
        break
    target_list.append(n)
    
    
length=len(target_list)

for i in range(0,length):
    tar_str=str(target_list[i])
    if tar_str==tar_str[::-1]:
        print("yes")
    else:
        print("no")
