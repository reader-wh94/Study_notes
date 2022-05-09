# https://programmers.co.kr/learn/courses/30/lessons/42842

def solution(brown, yellow):
  wl_list = []
  sub = []
  sum = brown + yellow
  
  for i in range(1, int(sum ** 0.5) + 1):
    if sum % i == 0:
      wid = int(sum / i)
      leng = i
      if wid >= leng:
        wl_list.append([wid, leng])
  
  for i in range(len(wl_list)):
    sub.append(wl_list[i][0] - wl_list[i][1])
  
  return wl_list[sub.index(min(sub))]

# 테스트 4,6,7 실패

# 2a + 2b - 4 = brown 이고
# (x-2)(y-2) == yellow 여야 한다.
def solution2(brown, yellow):
  sum = brown + yellow
  
  for i in range(1, sum+1):
    if sum % i == 0:
      a = int(sum / i)
      if a >= i:
        if (a - 2)*(i - 2) == yellow:
          return [a,i]

# https://dev-note-97.tistory.com/87