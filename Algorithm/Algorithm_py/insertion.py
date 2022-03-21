#삽입 정렬
def insertion(arr):
  n = len(arr)
  
  for i in range(1, n):
    j = i
    temp = arr[i]
    while j > 0 and arr[j-1] > temp:
      arr[j] = arr[j - 1]
      j -= 1
    arr[j] = temp
    
#test
arr = [5, 77, 85, 10, 1, 65, 99]
insertion(arr)
print(arr)