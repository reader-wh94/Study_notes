# https://programmers.co.kr/learn/courses/30/lessons/72410?language=python3
import re

def solution(new_id):
  answer = new_id
  answer = answer.lower()
  answer = re.sub('[^a-z0-9\-_.]', '', answer)
  answer = re.sub('\.+', '', answer)
  answer = answer.strip('.')
  
  if len(answer) <= 0:
    answer += 'a'
  
  if len(answer) >= 16:
    answer = answer[ :15]
    answer = answer.rstrip('.')
  elif len(answer) <=2:
    while len(answer) < 3:
      answer += answer[-1]
   
  return answer

solution('=.=')
