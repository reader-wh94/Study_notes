#버블 정렬
def bubble_sort(arr):
  n = len(arr)
  
  for i in range(n-1):
    # range(시작 숫자, 종류 숫자, step)
    for j in range(n-1, i, -1):
      if arr[j - 1] > arr[j]:
        arr[j-1], arr[j] = arr[j], arr[j-1]
        
# 최적화1 - 이전 패스에서 swap이 한 번도 일어나지 안았다면 정렬되지 않은 값이 하나도 없었다고 간주(패스 수행X)
def bubble_sort2(arr):
  n = len(arr)
  
  for i in range(n-1):
    swapped = False
    for j in range(n-1, i , -1):
      if arr[j-1] > arr[j]:
        arr[j-1], arr[j]=arr[j], arr[j-1]
        swapped = True
      if not swapped:
        break
      
#최적화2 - 이미 정렬된 원소를 제외한 나머지만 비교, 교환하도록 스캔 범위를 제한
def bubble_sort3(arr):
  n = len(arr)
  k = 0
  while k < n-1:
    last = n - 1
    for j in range(n-1, k, -1):
      if arr[j-1] > arr[j]:
        arr[j-1], arr[j]=arr[j], arr[j-1]
        last = j
    k = last  
