import sys
import queue
from itertools import permutations

string=sys.stdin.readline().rstrip().replace("\"","")
string_list=list(string)

def make_bracket(string_list,keyword):
    #우선순위 별로 괄호를 쳐주면 되겠다!!!
    #괄호를 치기 위해서는 일단 어느 인덱스에 어느 수식이 있는지 정보를 저장해야겠다.
    #[+,index] 형태의 2차원 배열이 들어가있음
    #3*2+3+25-100
    #3*(2+(3)+25)-100
    target_list=[]
    for x in range(0,len(string)):
        if string_list[x] == '+':
            target_list.append(['+',x])
        if string_list[x] == '-':
            target_list.append(['-',x])
        if string_list[x] == '*':
            target_list.append(['*',x])
    #target_list=[[*,1],[+,3],[+,5],[-,8]]

    #우선순위를 설정해보자
    #일단 나는 + > - > * 이렇게 선언할거임
    #주어진 string 중에 +가 어디 들어있는지 찾아서 인덱스값을 모아
    target_index=[]
    for x in range(0,len(target_list)):
        if target_list[x][0]==keyword:
            target_index.append(x)

    #len(target_list)=4
    #target_index=[1,2]
    #target_index를 기준으로 양쪽에 괄호를 씌워준다.        
    #새로운 괄호를 추가한 스택을 만들거임
    
    #찾는 수식어가 없는경우 그대로 return한다.
    if len(target_index) ==0:
        return string_list
    #print(target_index)
    for x in target_index:
        if x==0:
            string_list.insert(0,"(")
            for y in target_list:
                if y[1]>target_list[x-1][1]+1:
                    y[1]=y[1]+1
        else:
            string_list.insert(target_list[x-1][1]+1,"(")
            for y in target_list:
                if y[1]>target_list[x-1][1]+1:
                    y[1]=y[1]+1
        #target_list=[[*,1],[+,4],[+,6],[-,9]]
        #3*(2+3+25-100
        
        #target_list=[[*,1],[+,4],[+,8],[+,11]]
        #3*(2+(3)+25-100
        if x==len(target_list)-1:
            string_list.append(")")
            return string_list
        else:
            string_list.insert(target_list[x+1][1]-1,")")
        for y in target_list:
            if y[1]>target_list[x+1][1]-1:
                y[1]=y[1]+1
        #target_list=[[*,1],[+,4],[+,7],[-,10]]
        #3*(2+3)+25-100
        #target_list=[[*,1],[+,4],[+,8],[-,12]]
        #3*(2+(3)+25)-100
    #print(string_list)
    return string_list

dataset = ['+', '-', '*']
res = list(permutations(dataset, 3)) 
result=[]



for x in res:
    a=make_bracket(string_list,x[0]) 
    b=make_bracket(a,x[1])
    c=make_bracket(b,x[2])
    str=''.join(c)
    print(str)
    result.append(data=abs(eval(str)))
print(max(result))

#총 6번정도의 변환작업 후 값비교 -> 제일 큰거 제출
#eval() : 실행가능한 문자열을 인자로 받아 실행하는 함수
#abs() : 절댓값
