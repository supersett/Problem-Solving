
n=int(input())
#target=[]

for x in range(n):
    h,w,n=map(int,input().split())
    
    i=(n//h)+1
    j=n%h
    
    if j==0:
        i-=1
        j=h
    if i<10:
        print(str(j)+"0"+str(i))
        continue
    print(str(j)+str(i))
    

#target=[[6, 12, 10], [30, 50, 72]]
##
# def sol(list):
#     x=list[0]
#     y=list[1]
#     z=list[2]
#     hosu=(z//x)+1
#     stair=z%x
#     tr=""
#     if stair==0:
#         stair=x
#         hosu-=1
#     if len(str(hosu))==1:
#         tr="0"+str(hosu)
#     print(str(stair)+tr)

# for i in target:
#     sol(i)
