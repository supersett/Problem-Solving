import sys

n=int(input())

st=[]
an=[]
for _ in range(n):
    k=sys.stdin.readline().rstrip()
    if "push" in k:
        n,m=k.split()
        st.append(m)
    elif k=="pop":
        #if not st
        if len(st)==0:
            an.append(-1)
        else:
            an.append(st.pop())
    elif k=="size":
        an.append(len(st))
    elif k=="empty":
        if not st:
            an.append(1)
        else:
            an.append(0)
    elif k=="top":
        if not st:
            an.append(-1)
        else:
            an.append(st[-1])

for _ in an:
    print(_)