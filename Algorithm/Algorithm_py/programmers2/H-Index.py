# https://programmers.co.kr/learn/courses/30/lessons/42747
def solution(citations):
  citations.sort(reverse=True)
  
  for idx, citation in enumerate(citations):
    if idx >= citation:
      return idx
  
  return len(citations)

# 전체 논문 중 많이 인용된 순으로 정렬한 후, 
# 피인용수(citiation)가 논문 수와 같아지거나 
# 피인용수가 논문 수보다 작아지기 시작하는 숫자가 h