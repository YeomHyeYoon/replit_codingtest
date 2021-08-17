# 떡볶이 떡 만들기 p.201

# 떡 개수 n, 요청한 떡의 길이 m 입력받기
n,m = map(int,input().split())
# 각 떡의 개별 높이 정보 입력받기
hs = list(map(int,input().split()))

# 이진 탐색을 위한 시작점과 끝점 설정
hs.sort()
start = 0
end = hs[-1] # end = max(hs)

# 이진 탐색 수행
result = 0
while(start <= end):
  total = 0
  mid = (start+end)//2

  for x in hs :
    if x > mid :
      total += x - mid

  if total < m :
    end = mid -1

  else :
    result = mid # 최대한 덜 잘랐을 때가 정답이므로 여기에서 result 기록
    start = mid + 1

print(result)