# 미로 탈출 p.152

from collections import deque

#입력받기
n,m = map(int,input().split())

#맵 입력 받기
data = []
for i in range(n):
  data.append( list(map(int,input())))

#기본 값 세팅
x,y = 1,1

#이동 방향세팅
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(x,y):
  queue = deque()
  queue.append((x,y))
  while queue:
    x,y = queue.popleft()
    #현재 위치에서 4방향 확인
    for i in range(len(dx)):
      nx = x + dx[i]
      ny = y + dy[i]
      #공간 벗어나면 무시
      if nx<0 or nx >=n or ny<0 or ny>=m:
        continue
      #위치에 괴물이 있을 시
      if data[nx][ny] == 0:
        continue
      # 방문가능하고 방문하지 않았으면 최단거리 기록
      if data[nx][ny] == 1:
        data[nx][ny] = data[x][y]+1
        queue.append((nx,ny))
  #가장 오른쪽 아래까지의 최단 거리 반환
  return data[n-1][m-1]

print(bfs(0,0))