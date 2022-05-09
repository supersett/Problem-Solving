import sys
n=sys.stdin.readline()
a='c='
b='c-'
c='dz='
d='d-'
e='lj'
f='nj'
g='s='
h='z='
data=[a,b,c,d,e,f,g,h]
count=0
for i in data:
    val=n.find(i)
    if val!=-1:
        n.replace(i,'')
        count+=1
print(n)
for x in range(len(n)):
    count+=1
print(count)
