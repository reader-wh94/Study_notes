# https://www.acmicpc.net/problem/13913
from collections import deque

n, k = map(int, input().split())
visited = [0] * 100001
check = [0] * 100001

def bfs():
    q = deque([n])
    visited[n] = 1
    ans = []

    while q:
        x = q.popleft()

        if x == k:
            print(visited[x] - 1)
            while x != n:
                ans.append(x)
                x = check[x]
            ans.append(n)
            ans.reverse()

            print(ans)
            break

        for i in (2*x, x+1, x-1):
            if 0 <= i < 100001 and visited[i] == 0:
                visited[i] = visited[x] + 1
                q.append(i)
                check[i] = x
                # check[i]에 check[i] 오기 전 좌표를 저장(이전 위치)

bfs()