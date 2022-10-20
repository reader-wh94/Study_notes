import sys
input = sys.stdin.readline

n = int(input())
length = list(map(int, input().split()))
gas = list(map(int, input().split()))

res = 0
m = gas[0]

for i in range(n-1):
    if gas[i] < m:
        m = gas[i]
    res += m * length[i]

print(res)