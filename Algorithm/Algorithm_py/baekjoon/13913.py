# https://www.acmicpc.net/problem/13913
from collections import deque

n, k = map(int, input().split())
visited = [0] * 100001
check = [0] * 100001

def bfs():
    q = deque()
    q.append(n)

    visited[n] = 1

    while q:
        x = q.popleft()

        if x == k:
            print(visited[x] - 1)
            ans = []
            # check에 저장딘 경로 값을 통해 거슬러 올라가면서 ans에 저장
            while x != n:
                ans.append(x)
                x = check[x]
            ans.append(n)
            ans.reverse() # 역순으로 저장되어 있기 때문에 순서를 바꿈
            print(' '.join(map(str, ans)))
            return

        for i in (2*x, x-1, x+1):
            if 0 <= i < 100001 and visited[i] == 0:
                visited[i] = visited[x] + 1
                q.append(i)
                check[i] = x # 최종 경로 출력 시 i 값을 통해 이전 위치를 알아낼 수 있도록 저장

bfs()