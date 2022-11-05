import collections
def solution(n, student, point):
    answer = 0
    score_student_woo = collections.defaultdict(list)
    score_student_yul = collections.defaultdict(list)

    student_score_woo = collections.defaultdict(int)
    student_score_yul = collections.defaultdict(int)
    for i in range(1, n//2 + 1):
        score_student_woo[0].append(i)
        student_score_woo[i] = 0
    for i in range(n//2 + 1, n + 1):
        score_student_yul[0].append(i)
        student_score_yul[i] = 0
    stack = collections.deque([])
    for i in range(len(student)):
        for i in score_student_woo.keys():
            if not score_student_woo[i]:
               stack.append(i)
        while stack:
            score_student_woo.pop(stack.pop())
        for i in score_student_yul.keys():
            if not score_student_yul[i]:
                stack.append(i)
        while stack:
            score_student_yul.pop(stack.pop())
        this_student = student[i]
        this_point = point[i]
        # 우반에 있으면 걍 우반에 있자나
        if this_student in student_score_woo.keys():
            before_point = student_score_woo[this_student]
            score_student_woo[before_point].remove(this_student)
            score_student_woo[before_point + this_point].append(this_student)
            student_score_woo[this_student] += this_point
            continue
        # 열반에 있으면 우반에 갈 수도
        else:
            # 열반시절 나의 값
            this_before_point = student_score_yul[this_student]
            # 우반으로 가자~
            if this_point + this_before_point > min(score_student_woo.keys()):
                answer += 1

                # 열반에서 빼내보자 우선
                score_student_yul[this_before_point].remove(this_student)
                student_score_yul.pop(this_student)

                new_point = this_before_point + this_point

                # 우반에서 빼낼아이 찾자

                change_student = max(score_student_woo[min(score_student_woo.keys())])
                score_student_woo[min(score_student_woo.keys())].remove(change_student)
                change_score = student_score_woo[change_student]
                student_score_woo.pop(change_student)

                score_student_woo[new_point].append(this_student)
                student_score_woo[this_student] = new_point

                score_student_yul[change_score].append(change_student)
                student_score_yul[change_student] = change_score
                continue
            elif this_point + this_before_point == min(score_student_woo.keys()):
                if this_student < max(score_student_woo[min(score_student_woo.keys())]):
                    answer += 1

                    # 열반에서 빼내보자 우선
                    score_student_yul[this_before_point].remove(this_student)
                    student_score_yul.pop(this_student)

                    new_point = this_before_point + this_point

                    # 우반에서 빼낼아이 찾자

                    change_student = max(score_student_woo[min(score_student_woo.keys())])
                    score_student_woo[min(score_student_woo.keys())].remove(change_student)
                    change_score = student_score_woo[change_student]
                    student_score_woo.pop(change_student)

                    score_student_woo[new_point].append(this_student)
                    student_score_woo[this_student] = new_point

                    score_student_yul[change_score].append(change_student)
                    student_score_yul[change_student] = change_score
                    continue
        score_student_yul[this_before_point].remove(this_student)
        score_student_yul[this_before_point + this_point].append(this_student)
        student_score_yul[this_student] = this_before_point + this_point  
    return answer

print(solution(6,[6,1,4,2,5,1,3,3,1,6,5],[3,2,5,3,4,2,4,2,3,2,2]))