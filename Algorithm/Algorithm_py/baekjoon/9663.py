# https://www.acmicpc.net/problem/9663

def check(x):
  for i in range(x):
    if graph[x] == graph[i] or abs(graph[x] - graph[i]) == x - i:
      return False
  return True

def queen(x):
  global result
  if x == N:
    result += 1
    return
  else:
    for i in range(N):
      graph[x] = i
      if check(x):
        queen(x + 1)

N = int(input())
graph = [0] * N
result = 0
queen(0)
print(result)
