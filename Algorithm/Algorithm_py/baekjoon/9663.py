# https://www.acmicpc.net/problem/9663

def check(x):
  for i in range(x):
    if graph[x] == graph[i] or abs(graph[x] - graph[i]) == x - i:
      return False
  return True

def dfs(x):
  global result
  
  if x == N:
    result += 1
    return
  else:
    for i in range(N):
      graph[x] = i
      if check(x):
        dfs(x + 1)

N = int(input())
graph = [0] * N
result = 0
dfs(0)
print(result)

# check 함수가 잘 이해가 안됐다
# python3으로 제출하니까 시간초과가 났고, PyPy3으로 했더니 겨우 통과했다.