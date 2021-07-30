# 왕실의 나이트 p114

#입력 받기
n = input()

# x는 열
x= int(n[1])

# y는 행.문자열 입력을 숫자로 바꾸기 위함
a = ["a","b","c","d","e","f","g","h"]

for i in range(len(a)):
  if n[0] == a[i]:
    y=i+1


# 이동가능한 좌표 표현
dx = [-2,-2,2,2,-1,-1,1,1]
dy = [1,-1,1,-1,2,-2,2,-2]

# 이동가능한 좌표 표현2
steps = [(-2,1),(-2,-1),(2,1),(2,-1),(-1,2),(-1,-2),(1,2),(1,-2)]

count = 0

# 이동가능한 좌표수만큼 반복하면서 이동가능한지 확인
for i in range(len(dx)):
  nx = x + dx[i]
  ny = y + dy[i]

  # 이동 불가시 카운트하지 않음
  if nx<1 or ny<1 or nx>8 or ny>8:
    continue
  
  count += 1

# 이동 가능한 수 카운트 최종 출력
print(count)