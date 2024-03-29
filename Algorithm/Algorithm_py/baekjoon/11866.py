# https://www.acmicpc.net/problem/11866

from collections import deque

n, k = map(int, input().split())
q = deque([])
ans = []

for i in range(1, n+1):
    q.append(i)

while q:
    for i in range(k-1):
        q.append(q.popleft())
    ans.append(q.popleft())

print('<', end='')
print(', '.join(map(str, ans)), end='')
print('>')