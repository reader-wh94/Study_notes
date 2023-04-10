# https://translate.google.co.kr/?hl=ko&sl=ko&tl=en&text=%EC%8B%A4%ED%8C%A8%EC%9C%A8&op=translate

def solution(N, stages):
  answer = []
  rate = []
  dic = dict()
  length = len(stages)
  
  for i in range(1, N+2):
    if(i == N + 1):
      continue
    rate.append(stages.count(i))
    
  for i in range(len(rate)):
    if(length == 0):
      dic[i+1] = 0
    else:
      r = rate[i] / length
      length -= rate[i]
      dic[i+1] = r
  
  dic2 = sorted(dic.items(), key=lambda x: x[1], reverse=True)
  
  for key, value in dic2:
    answer.append(key)
  
  return answer