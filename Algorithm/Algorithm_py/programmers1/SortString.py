# https://programmers.co.kr/learn/courses/30/lessons/12917?language=python3
def solution(s):
  arr = list(s)
  arr.sort(reverse=True)
  answer = ''.join(arr)
  return answer