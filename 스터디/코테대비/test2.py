import sys
n=sys.stdin.readline().rstrip().replace("\"","")
listn=list(n)

def make_bracket(string_list,keyword):
    hand_string_list=string_list
    target_list=[]
    for x in range(0,len(hand_string_list)):
        if hand_string_list[x] == '+':
            target_list.append(['+',x])
        if hand_string_list[x] == '-':
            target_list.append(['-',x])
        if hand_string_list[x] == '*':
            target_list.append(['*',x])
    target_index=[]
    for x in range(0,len(target_list)):
        if target_list[x][0]==keyword:
            target_index.append(x)
    print(target_index)
    if len(target_index) ==0:
        print("해당문자 없어!")
        return string_list
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
            if x==len(target_list)-1:
                hand_string_list.append(")")
                return hand_string_list
            else:
                hand_string_list.insert(target_list[x+1][1],")")
            for y in target_list:
                if y[1]>target_list[x+1][1]-1:
                    y[1]=y[1]+1
        new_string_list=hand_string_list
        return new_string_list