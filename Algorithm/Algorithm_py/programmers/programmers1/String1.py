# https://programmers.co.kr/learn/courses/30/lessons/12918?language=python3
def solution(s):
  answer = True
  return s.isdigit() and (len(s) == 4 or len(s) == 6)