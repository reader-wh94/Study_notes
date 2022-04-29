# https://programmers.co.kr/learn/courses/30/lessons/12939?language=python3
def solution(s):
  num = s.split(' ')
  num = [int(i) for i in num]
  
  min_s = str(min(num))
  max_S = str(max(num))
  
  return min_s + ' ' + max_S