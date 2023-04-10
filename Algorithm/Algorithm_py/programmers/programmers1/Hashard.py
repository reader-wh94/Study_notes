# https://programmers.co.kr/learn/courses/30/lessons/12947?language=python3
def solution(x):
  answer = True
  sum = 0
  x_list = list(map(int, str(x)))
  
  for i in x_list:
    sum += i
  
  if x % sum != 0:
    answer = False
  
  return answer