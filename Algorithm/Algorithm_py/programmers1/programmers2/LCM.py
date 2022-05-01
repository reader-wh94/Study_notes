# https://programmers.co.kr/learn/courses/30/lessons/12953?language=python3
def solution(arr):
  answer = arr[0]
  
  for i in range(1, len(arr)):
    for j in range(arr[i], answer * arr[i] + 1, arr[i]):
      if j % answer == 0 and j % arr[i] == 0:
        answer = j
        break

  return answer