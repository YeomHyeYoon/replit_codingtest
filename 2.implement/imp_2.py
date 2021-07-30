# 시각 p113

#시간 입력받기
n = int(input())

#카운트 초기화
count = 0 

# n시까지 3이 들어간 횟수 카운트
for i in range(n+1):
  for j in range(60):
    for z in range(60):
      if '3' in str(i)+str(j)+str(z) :
        count += 1

  

print(count)