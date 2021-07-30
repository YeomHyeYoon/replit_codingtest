# 구현-상하좌우 문제 p110

# 행렬 크기 입력 받기. N*N 행렬 생성
n = int(input())

#기본 위치 초기화
dx,dy = 1,1

# 입력받은걸 리스트에 넣고  하나씩 빼내면서 값을 확인
datas = input().split()

# 만약에 L이면 열 -1 이니까 dy -1
# 만약에 R이면 열 +1 이니까 dy +1
# 만약에 U이면 행 -1 이니까 dx -1
# 만약에 D이면 행 +1 이니까 dx +1
# x,y 좌표가 n보다 크거나 1보다 작으면 안됨!
for data in datas:

  if data == "L":
    dy -= 1
    if not(dy>=1 and dy<=n):
      dy += 1

  if data == "R":
    dy += 1
    if not(dy>=1 and dy<=n):
      dy -= 1

  if data == "U":
    dx -= 1
    if not(dx>=1 and dx<=n):
      dx += 1
  
  if data == "D":
    dx += 1
    if not(dx>=1 and dx<=n):
      dx -= 1

#최종 출력 
print(dx,dy)