# https://programmers.co.kr/learn/courses/30/lessons/12934?language=python3

def solution(n):
  answer = -1
  x = n**(1/2)
  
  if x == int(x):
    # 제곱근의 정수 부분만을 비교(음수나 3,5 등의 경우는 소수점으로 나오기 때문)
    answer = (x+1)**2
  return answer

print(solution(121))