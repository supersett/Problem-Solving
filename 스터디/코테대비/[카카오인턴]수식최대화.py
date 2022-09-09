import sys
import queue
from itertools import permutations

string_input=sys.stdin.readline().rstrip().replace("\"","")
string_listtt=list(string_input)
tq=string_listtt

def calculate_bracket(string_given):
    try:
        count=string_given.count("(")
        calculate_list_index=[]
        #print(count)
        what_we_want=string_given
        for i in range(0,count):
            #print(i)
            for x in range(0,len(what_we_want)):
                if what_we_want[x]=="(":
                    calculate_list_index.append(x)
                if what_we_want[x]==")":
                    calculate_list_index.append(x)
                    #print(calculate_list_index)
                    #괄호로 묶인부분 합해주는 부분
                    lista=what_we_want[(calculate_list_index[0]+1):(calculate_list_index[1])]
                    #print(lista)
                    s=''.join(lista)
                    #print(s)
                    data=eval(s)
                    #print(data)
                    data_string=str(data)
                    #(500-100) -> 400 으로 바꿔주는 부분
                    target=''.join(what_we_want[calculate_list_index[0]:calculate_list_index[1]+1])
                    #print(target)
                    sumver_string_given=''.join(what_we_want)
                    sumver_string_given=sumver_string_given.replace(target,data_string)
                    target_list=list(sumver_string_given)
                    what_we_want=target_list
                    #print(target_list)
                    calculate_list_index.clear()
                    break
        #print(what_we_want)
        return what_we_want
    except SyntaxError:
        

def make_bracket(string_list,keyword):
    #우선순위 별로 괄호를 쳐주면 되겠다!!!
    #괄호를 치기 위해서는 일단 어느 인덱스에 어느 수식이 있는지 정보를 저장해야겠다.
    #[+,index] 형태의 2차원 배열이 들어가있음
    #3*2+3+25-100
    #3*(2+(3)+25)-100
    hand_string_list=string_list
    target_list=[]
    for x in range(0,len(hand_string_list)):
        if hand_string_list[x] == '+':
            target_list.append(['+',x])
        if hand_string_list[x] == '-':
            target_list.append(['-',x])
        if hand_string_list[x] == '*':
            target_list.append(['*',x])
    #target_list=[[*,1],[+,3],[+,5],[-,8]]

    #우선순위를 설정해보자
    #일단 나는 + > - > * 이렇게 선언할거임
    #주어진 string 중에 +가 어디 들어있는지 찾아서 인덱스값을 모아
    target_index=[]
    for x in range(0,len(target_list)):
        if target_list[x][0]==keyword:
            target_index.append(x)
    print(target_index)
    #len(target_list)=4
    #target_index=[1,2]
    #target_index를 기준으로 양쪽에 괄호를 씌워준다.        
    #새로운 괄호를 추가한 스택을 만들거임
    
    #찾는 수식어가 없는경우 그대로 return한다.
    if len(target_index) ==0:
        print("해당문자 없어!")
        return string_list
    #print(target_index)
    else:
        for x in target_index:
            if x==0:
                hand_string_list.insert(0,"(")
                for y in target_list:
                    y[1]=y[1]+1
            else:
                hand_string_list.insert(target_list[x-1][1]+1,"(")
                for y in target_list:
                    if y[1]>target_list[x-1][1]+1:
                        y[1]=y[1]+1
            #target_list=[[*,1],[+,4],[+,6],[-,9]]
            #3*(2+3+25-100
            
            #target_list=[[*,1],[+,4],[+,8],[+,11]]
            #3*(2+(3)+25-100
            if x==len(target_list)-1:
                hand_string_list.append(")")
                return hand_string_list
            else:
                hand_string_list.insert(target_list[x+1][1],")")
            for y in target_list:
                if y[1]>target_list[x+1][1]-1:
                    y[1]=y[1]+1
            #target_list=[[*,1],[+,4],[+,7],[-,10]]
            #3*(2+3)+25-100
            #target_list=[[*,1],[+,4],[+,8],[-,12]]
            #3*(2+(3)+25)-100
        new_string_list=hand_string_list
        return new_string_list

dataset = ['*','+', '-' ]
res = list(permutations(dataset, 3)) 
result=[]



for x in res:
    print(tq)
    print("처음키워드="+x[0])
    print("두번째키워드"+x[1])
    print("세번째키워드"+x[2])
    a=make_bracket(tq,x[0])
    print(a)
    print(calculate_bracket(a))
    b=make_bracket(calculate_bracket(a),x[1])
    print(b)
    print(calculate_bracket(b))
    c=make_bracket(calculate_bracket(b),x[2])
    strr=''.join(c)
    print(strr)
    result.append(abs(eval(strr)))
    print(result)
    tq.remove("(")
    tq.remove(")")
    






#총 6번정도의 변환작업 후 값비교 -> 제일 큰거 제출
#eval() : 실행가능한 문자열을 인자로 받아 실행하는 함수
#abs() : 절댓값
