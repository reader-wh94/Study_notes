# https://programmers.co.kr/learn/courses/30/lessons/12935?language=python3

def solution(arr):
  answer = []
  
  if len(arr) > 1:
    idx = arr.index(min(arr))
    del arr[idx]
    answer = arr
  else:
    answer = [-1]
      
  return answer