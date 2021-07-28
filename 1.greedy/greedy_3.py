# 큰 수의 법칙 p.92

n,m,k = map(int,input().split())

data = list(map(int , input().split()))

data.sort() #입력받은 수들 정렬하기
first = data[n-1]
second = data[n-2]

result = 0

while True :
  for i in range(k): # 가장 큰 수 k번 더하기
    if m == 0: # m번 더하는 것이기에 0번시 반복문 탈출
      break
    result += first
    m -= 1
  if m==0:
    break
  result += second # 두 번째로 큰 수를 한 번 더하기
  m -=1

print(result)


