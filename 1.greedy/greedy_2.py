#숫자카드게임 p.96

# 행 n , 열 m 입력
n,m = map(int , input().split())
result = 0

# 행마다 입력 받기
for i in range(n):
  data = list(map(int , input().split()))
  min_value = min(data) # 현재 줄에서 '가장 작은 수' 찾기
  result = max(min_value , result) # '가장 작은 수'들 중에서 가장 큰 수 찾기

print(result)