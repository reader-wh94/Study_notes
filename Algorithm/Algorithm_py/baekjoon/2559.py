# https://www.acmicpc.net/problem/2559
import sys

n, k = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
res = [sum(arr[:k])]

for i in range(n - k):
    res.append(res[i] - arr[i] + arr[k+i])

print(max(res))

# 방법은 똑같이 생각났는데 구현을 못함ㅎ list 쓰는 법 아는데... why...

