import sys

def solution(text):
    answer = 0
    return answer

n=sys.stdin.readline().rstrip()
target_list=list(n)
count=0

print(n)
print(target_list)
for x in target_list:
    if x=="a":
        count+=1
    elif x =="e":
        count+=1
    elif x =="i":
        count+=1
    elif x == "o":
        count+=1
    elif x == "u":
        count+=1
    

print(count)