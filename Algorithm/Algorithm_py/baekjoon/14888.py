# https://www.acmicpc.net/problem/14888
import sys

n = int(input())
numbers = list(map(int, sys.stdin.readline().split()))
operator = list(map(int, sys.stdin.readline().split()))
minAns = float('Inf')
maxAns = float('-Inf')

def dfs(index, res):
    global minAns
    global maxAns

    if index == n-1:
        if minAns > res:
            minAns = res
        if maxAns < res:
            maxAns = res
        return res

    for i in range(4):
        temp = res
        if operator[i] == 0:
            continue
        if i == 0:
            res += numbers[index+1]
        elif i == 1:
            res -= numbers[index+1]
        elif i == 2:
            res *= numbers[index+1]
        else:
            if res < 0:
                res = abs(res) // numbers[index+1] * (-1)
            else:
                res //= numbers[index+1]

        operator[i] -= 1
        dfs(index+1, res)
        operator[i] += 1
        res = temp

dfs(0, numbers[0])
print(maxAns)
print(minAns)