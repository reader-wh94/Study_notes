# https://programmers.co.kr/learn/courses/30/lessons/12949?language=python3

def solution(arr1, arr2):
  answer = []
  
  for x in range(len(arr1)):
    arr = []
    for y in range(len(arr2[0])):
      sum = 0
      for i in range(len(arr1[0])):
        sum += arr1[x][i] * arr2[i][y]
      arr.append(sum)
    answer.append(arr)
  
  return answer