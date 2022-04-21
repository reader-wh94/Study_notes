# https://programmers.co.kr/learn/courses/30/lessons/81301?language=python3
def solution(s):
  answer = 0
  eng = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
  
  for i in range(len(eng)):
    s = s.replace(eng[i], str(i))
  answer = int(s)
  return answer