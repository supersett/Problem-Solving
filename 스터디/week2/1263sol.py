N = int(input())
schedule = []

# 일정 소요시간과 완료해야하는 시간 schedule에 저장
for _ in range(N):
    T, S = map(int, input().split())
    schedule.append([T, S])

# 일정을 완료해야하는 순으로 정렬
schedule = sorted(schedule, key=lambda x:x[1])
print(schedule)
#일정 시작시간
time = 0
while 1:
    # time만큼 늦게 시작함
    sumTime = time

    #전체 일정들에 대해
    for t, s in schedule:
        # 해당 일정을 제 시간안에 처리할 수 있으면 소요시간+t
        if sumTime+t <= s:
            sumTime += t
        else:
            # 늦게 시작했을 때 완료하지 못하면
            # 시작 시간보다 1시간 일찍 시작하는것으로 출력
            # 0시에 시작했는데도 완료하지 못하면 -1 출력
            print(time-1)
            exit()
    time += 1