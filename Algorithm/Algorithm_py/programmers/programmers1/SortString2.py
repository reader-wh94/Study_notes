# https://programmers.co.kr/learn/courses/30/lessons/12915?language=python3
def solution(strings, n):
  answer = []
  
  for i in strings:
    answer.append(i[n:n+1] + i)
  
  answer.sort()
  
  for index, value in enumerate(answer):
    answer[index] = value[1:]
    
  return answer