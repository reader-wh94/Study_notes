# https://programmers.co.kr/learn/courses/30/lessons/12912?language=python3
def solution(a, b):
  answer = 0
  
  if a == b:
    answer = a
  else:
    scope = abs(a-b) + 1
    x = min(a,b)
    
    for i in range(x, x + scope):
      answer += i
  
  return answer

# sum 내장 함수가 있는 걸 까먹었다