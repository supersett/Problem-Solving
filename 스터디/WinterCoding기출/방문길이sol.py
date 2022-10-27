def solution(dirs):
  answer=0
  x,y=5,5
  dic={"U":[0,1],"D":[0,-1],"L":[-1,0],"R":[1,0]}
  target_set=set()
  
  for i in dirs:
    nx=dic[i][0]+x
    ny=dic[i][1]+y
    
    if nx<0 or nx>=11 or ny>=11 or ny<0:
      nx,ny=x,y
      continue
    if (x,y,nx,ny) not in target_set:
      target_set.add((x,y,nx,ny))
      target_set.add((nx,ny,x,y))
      answer+=1
    x,y=nx,ny
  
  return answer