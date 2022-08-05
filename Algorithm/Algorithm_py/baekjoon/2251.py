# https://www.acmicpc.net/problem/2251
from collections import deque

a, b, c = map(int, input().split())
visited = [[False] * (b+1) for _ in range(a+1)]
q = deque()
res = []

q.append((0, 0))
visited[0][0] = True

def pour(x, y):
    if not visited[x][y]:
        visited[x][y] = True
        q.append((x, y))

def bfs():
    while q:
        aa, bb = q.popleft()
        cc = c - aa - bb

        if aa == 0:
            res.append(cc)

        # A에서 B로 이동
        water = min(aa, b - bb)
        pour(aa - water, bb + water)

        # A에서 C로 이동
        water = min(aa, c - cc)
        pour(aa - water, bb)

        # B에서 A로 이동
        water = min(bb, a - aa)
        pour(aa + water, bb - water)

        # B에서 C로 이동
        water = min(bb, c - cc)
        pour(aa, bb - water)

        # C에서 A로 이동
        water = min(cc, a - aa)
        pour(aa + water, bb)

        # C에서 B로 이동
        water = min(cc, b - bb)
        pour(aa, bb + water)

bfs()
res.sort()
print(' '.join(map(str, res)))
