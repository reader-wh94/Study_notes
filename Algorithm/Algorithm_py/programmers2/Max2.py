# https://programmers.co.kr/learn/courses/30/lessons/42883

def solution(number, k):
  number_list = list(map(str, str(number)))
  
  for i in range(k):
    number_list.remove(min(number_list))
  
  answer = ''.join(number_list)
  
  return answer
# 리스트에서 가장 작은 수만 제거한 후 리턴 -> 가장 작은 수 제거보다 가장 큰 수를 만들어야 한다
# 1, 2번 예시 문제는 통과 되지만 3번은 통과되지 않음

def solution2(number, k):
  answer = [number[0]]
  
  for i in number[1:]:
    while len(answer) > 0 and answer[-1] < i and k > 0:
      k -= 1
      answer.pop()
    answer.append(i)
    
  if k != 0:
    answer = answer[:-k]      
  
  return ''.join(answer)
# https://eda-ai-lab.tistory.com/465
# 스택을 사용해서 조건에 맞는 값만 넣는 방법이 있다.