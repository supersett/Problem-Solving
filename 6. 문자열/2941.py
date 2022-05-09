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
        count+=1
        
for i in data:
    val=n.find(i)
    if val!=-1:
        n=n.replace(i," ")
n=n.replace(" ","")

for i in data:
    val=n.find(i)
    if val!=-1:
        count+=1
        
count=count+len(n)-1

print(count)
