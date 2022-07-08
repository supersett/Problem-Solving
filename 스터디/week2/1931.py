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
for i in range(n):
    cnt=1
    start_time=sch[i][0]
    end_time=sch[i][1]
    for j in range(i,n):
        if end_time==sch[j][0]:
            cnt+=1
            end_time=sch[j][1]
        elif end_time<=sch[j][0]:
            start_time=sch[j][0]
            end_time=sch[j][1]
            cnt+=1
    cnt_list.append(cnt)

print(max(cnt_list))