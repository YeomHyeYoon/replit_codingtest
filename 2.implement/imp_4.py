#입력 받기
n,m = map(int,input().split())

#현재 위치 및 방향 입력
x,y,d = map(int,input().split())

# 북,동,남,서
dx = [-1,0,1,0]
dy = [0,1,0,-1]

#방문할 곳 표시(방문한 곳도 나중엔 가면 안되기에 입력받을 맵말고 또다른 맵 생성)
visit = [[0]*n for _ in range(m)]

#현재위치는 이미 방문상태이기에 1로 세팅
visit[x][y] = 1

# 맵
data = [list(map(int,input().split())) for _ in range(n)]

#카운트 수 및 회전 수 세팅
count = 1
turn_time = 0

#왼쪽 회전 함수
def turn_left():
  global d
  d -= 1
  if d == -1:
    d = 3

while True:
  #왼쪽 회전
  turn_left()
  
  #회전 후 이동
  nx = x + dx[d]
  ny = y + dy[d]

  #이동후 0인 경우 (즉, 육지이면서 방문 안한 곳)
  if data[nx][ny]==0 and visit[nx][ny]==0 :
    visit[nx][ny] = 1
    x = nx
    y = ny
    count += 1
    turn_time = 0
    continue
  # 이동후 1인 경우 (바다이거나 방문 한 곳)
  else:
    turn_time += 1
  # 네방향 이미 가 본 곳이거나 바다인곳 (4방향모두 못가는 경우)
  if turn_time == 4:
    nx = x - dx[d]
    ny = y - dy[d]
    #뒤로갈 수 있으면 이동
    if data[nx][ny] ==0:
      x = nx
      y = ny
    #뒤로 못가면 움직임 멈춤
    else:
      break
    #네방향 모두 못가는 경우 처리 후 0으로 초기화
    turn_time = 0

print(count)