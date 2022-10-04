# https://www.acmicpc.net/problem/10986
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
numbers = list(map(int, input().split())) + [0]
count = [0] * m

for i in range(n):
    numbers[i] += numbers[i - 1]
    count[numbers[i] % m] += 1

answer = count[0]

for x in count:
    answer += x * (x-1) // 2

print(answer)