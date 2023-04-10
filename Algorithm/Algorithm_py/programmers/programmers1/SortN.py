# https://programmers.co.kr/learn/courses/30/lessons/12933

def solution(n):
  arr = list(str(int(n)))
  arr.sort(reverse=True)
  
  answer = int(''.join(arr)) 
  return answer
