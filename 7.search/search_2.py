# 부품 찾기 p.197

n = int(input())
my_data = list(map(int,input().split()))

my_data.sort()

m = int(input())
cl_data = list(map(int,input().split()))


def binary_search(array,target,start,end):
  while start <= end :
    mid = (start+end) // 2
    
    if array[mid] == target :
      return mid

    elif array[mid] > target :
      end = mid - 1
    
    else :
      start = mid +1
  return None 

for i in cl_data :
  result = binary_search(my_data , i , 0 , n-1)
  if result != None :
    print('yes' , end =' ')
  else :
    print('no' , end=' ')

