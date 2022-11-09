# https://www.acmicpc.net/problem/5430
import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    fun = input()
    n = int(input())
    numbers = deque(input().rstrip()[1:-1].split(","))

    if n == 0:
        numbers = []

    reverse = 0
    flag = 0

    for i in fun:
        if i == 'R':
            reverse += 1
        elif i == 'D':
            if numbers:
                if reverse % 2 == 0:
                    numbers.popleft()
                else:
                    numbers.pop()
            else:
                print("error")
                flag = 1
                break
    if flag == 0:
        if reverse % 2 == 0:
            print("["+",".join(numbers)+"]")
        else:
            numbers.reverse()
            print("[" + ",".join(numbers) + "]")