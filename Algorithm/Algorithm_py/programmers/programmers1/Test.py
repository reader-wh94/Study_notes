# https://programmers.co.kr/learn/courses/30/lessons/42840?language=python3
def solution(answers):
  answer = []
  p1 = [1,2,3,4,5]
  p2 = [2,1,2,3,2,4,2,5]
  p3 = [3,3,1,1,2,2,4,4,5,5]
  score = [0,0,0]
  
  for idx, value in enumerate(answers):
    if value == p1[idx % len(p1)]:
      score[0] += 1
    if value == p2[idx % len(p2)]:
      score[1] += 1
    if value == p3[idx % len(p3)]:
      score[2] += 1
  
  m = max(score)
  answer = [i + 1 for i,v in enumerate(score) if v == m]
    
  return answer