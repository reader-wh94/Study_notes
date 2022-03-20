# 선택 정렬
def selection(arr):
  n = len(arr)
  
  for i in range(n-1):
    min = i
    for j in range(i + 1, n):
      if arr[j] < arr[min]:
        min = j
    arr[i], arr[min] = arr[min], arr[i]
      