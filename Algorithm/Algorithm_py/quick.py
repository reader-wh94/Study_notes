# 퀵 정렬

def quick1(arr, start, end):
  if start >= end:
    return
  
  pivot = start
  left = start + 1
  right = end
  while (left <= right): #left와 right가 교차하기 전까지
    while(left <= end and arr[left] <= arr[pivot]):
      #pivot보다 큰 데이터를 찾을 때까지 반복
      left += 1
    while(right > start and arr[right] >= arr[pivot]):
      #pivot보다 작은 데이터를 찾을 때까지 반복
      right -= 1
    if(left > right):
      #left와 right가 교차되었다면 작은 데이터와 피벗을 교체
      arr[right], arr[pivot] = arr[pivot], arr[right]
    else: 
      #교차되지 않았다면 작은 데이터와 큰 데이터를 교체
      arr[left], arr[right] = arr[right], arr[left]
  
  #분할 이후 왼쪽 부분과 오른쪽 부분 각각 정렬 수행
  quick1(arr, start, right - 1)
  quick1(arr, right + 1, end)


# 1번보다 더 직관적
def quick2(arr):
  if len(arr) <= 1:
    return arr
  
  pivot = arr[0]
  tail = arr[1:] #pivot 제외한 리스트
  
  left_side = [x for x in tail if x <= pivot]
  right_side = [x for x in tail if x > pivot]
  
  return quick2(left_side) + [pivot] + quick2(right_side)
