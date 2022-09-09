from itertools import permutations
import sys

def calculate_bracket(string_given):
    count=string_given.count("(")
    calculate_list_index=[]
    print(count)
    what_we_want=string_given
    for i in range(0,count):
        print(i)
        for x in range(0,len(what_we_want)):
            
            if what_we_want[x]=="(":
                calculate_list_index.append(x)
            if what_we_want[x]==")":
                calculate_list_index.append(x)
                print(calculate_list_index)
                #괄호로 묶인부분 합해주는 부분
                lista=what_we_want[(calculate_list_index[0]+1):(calculate_list_index[1])]
                print(lista)
                s=''.join(lista)
                print(s)
                data=eval(s)
                print(data)
                data_string=str(data)
                
                #(500-100) -> 400 으로 바꿔주는 부분
                target=''.join(what_we_want[calculate_list_index[0]:calculate_list_index[1]+1])
                print(target)
                sumver_string_given=''.join(what_we_want)
                sumver_string_given=sumver_string_given.replace(target,data_string)
                target_list=list(sumver_string_given)
                what_we_want=target_list
                print(target_list)
                calculate_list_index.clear()
                break
    print(what_we_want)
    return what_we_want

n=sys.stdin.readline().rstrip().replace("\"","")
print(n)
list_n=list(n)
calculate_bracket(list_n)

#"(500+100)-(400+400)"