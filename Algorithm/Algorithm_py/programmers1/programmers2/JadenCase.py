# https://programmers.co.kr/learn/courses/30/lessons/12951?language=python3
def solution(s):
  answer = ''
  x = 0
  
  for idx, value in enumerate(s):
    if idx == 0:
      if value.isalpha():
        answer += value.upper()
      else:
        answer += value
    else:
      if value == ' ':
        x = 1
        answer += value
      elif value != ' ' and x == 1:
        answer += value.upper()
        x = 0
      else:
        answer += value.lower()

  return answer