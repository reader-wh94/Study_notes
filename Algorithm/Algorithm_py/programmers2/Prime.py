# https://programmers.co.kr/learn/courses/30/lessons/42839
from itertools import permutations
import math

def solution(numbers):
  answer = 0
  nums = list(map(str, str(numbers)))
  per = []
  
  for i in range(1, len(numbers) + 1):
    per += list(permutations(nums, i))
  
  new_nums = list({int(''.join(x)) for x in per})
 
  for i in new_nums:
    if i < 2:
      continue
    check = True
    
    for j in range(2, int(math.sqrt(i)) + 1):
      if i % j == 0:
        check = False
        break
    if check:
      answer += 1

  return answer

# 순열로 해야할까 조합으로 해야할까? -> 조합은 (A,B) (B,A)를 같은 것으로 판단하니 순열로 풀자
# 순열 값들을 구하고 set으로 중복 제거 후 소수로 판별하기