# 특정 거리의 도시찾기 - BFS문제 p339

from collections import deque

n,m,k,x = map(int , input().split())

data = [[]for _ in range(n+1)]

for _ in range(m):
  a,b = map(int , input().split())
  data[a].append(b)

distance = [-1]*(n+1)
distance[x] = 0

#최단 거리 갱신
queue = deque([x])
while queue :
  now = queue.popleft()
  for next_node in data[now]:
    if distance[next_node] == -1:
      distance[next_node] = distance[now] +1
      queue.append(next_node)
  
# 최단 거리가 k인 도시 찾기  
check = False
for i in range(1,n+1):
  if distance[i] == k:
    print(i)
    check = True

# 최단 거리가 k인 도시가 없을 때
if check == False:
  print(-1)
    