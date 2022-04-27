# https://programmers.co.kr/learn/courses/30/lessons/12945?language=python3

def solution(n):
  a = 1
  b = 1
  if n == 1 and n == 2:
    return 1
  for i in range(1, n):
    a, b = b, b + a
    
  return a % 1234567