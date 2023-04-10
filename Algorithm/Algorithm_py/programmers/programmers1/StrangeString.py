# https://programmers.co.kr/learn/courses/30/lessons/12930?language=python3
from multiprocessing.sharedctypes import Value


def solution(s):
  answer = ''
  
  for word in s.split(' '):
    for i in range(len(word)):
      if i % 2 == 0:
        answer += word[i].upper()
      else:
        answer += word[i].lower()
    answer += ' '

  return answer[:-1]