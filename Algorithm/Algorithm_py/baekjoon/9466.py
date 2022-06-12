# https://www.acmicpc.net/problem/9466
import sys
sys.setrecursionlimit(100000)

T = int(input())

def dfs(x):
    global result
    visited[x] = True
    team.append(x)
    num = students[x]

    if visited[num] == True:
        if num in team:
            result += team[team.index(num):]
        return
    else:
        dfs(num)

for _ in range(T):
    N = int(input())
    students = [0] +  list(map(int, input().split()))
    visited = [True] + [False] * (N+1)
    result = []

    for i in range(1, N + 1):
        if visited[i] == False:
            team = []
            dfs(i)

    print(N - len(result))