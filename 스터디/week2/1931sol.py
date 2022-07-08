import sys

n=int(sys.stdin.readline())
sch=[]

#회의의 시작시간 S , 마치는시간 E 를 sch 배열에 담는다.
for i in range(n):
    S,T=map(int,sys.stdin.readline().split())
    sch.append([S,T])

#회의 시작시간 순으로 배열을 정렬한다.
sch=sorted(sch,key = lambda x: [x[1], x[0]])

#print(sch)
cnt_list=[]
cur_time=0
cnt=0
for i in range(n):
    if cur_time==sch[i][0]:
        cnt+=1
        cur_time=sch[i][1]
    elif cur_time<sch[i][0]:
        cnt+=1
        cur_time=sch[i][1]
print(cnt)
    
