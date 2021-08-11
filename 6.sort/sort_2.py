# p181 성적이 낮은 순서로 학생 출력하기

n = int(input())

array = []

for i in range(n):
  data = input().split()
  name = data[0]
  score = data[1]
  array.append((name,score))

def setting(data):
  return data[1]

result = sorted(array , key = setting )

for d in result:
  print(d[0] , end=' ')