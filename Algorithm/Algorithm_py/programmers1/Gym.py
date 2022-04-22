# https://programmers.co.kr/learn/courses/30/lessons/42862?language=python3

def solution(n, lost, reserve):
  r = [re for re in reserve]
  l = [lo for lo in lost]
  
  r.sort()
  l.sort()

  for i in lost:
    if r.count(i) != 0:
      r.remove(i)
      l.remove(i)
  
  for i in r:
    left = i - 1
    right = i + 1
    if left in l:
      l.remove(left)
    elif right in l:
      l.remove(right)
  
  return n - len(l)