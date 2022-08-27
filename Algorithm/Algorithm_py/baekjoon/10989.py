# https://www.acmicpc.net/problem/10989
import sys

n = int(sys.stdin.readline())
numbers = [0] * 10001

for i in range(n):
    numbers[int(sys.stdin.readline())] += 1

for i in range(10001):
    if numbers[i] != 0:
        for j in range(numbers[i]):
            print(i)