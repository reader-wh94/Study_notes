# https://www.acmicpc.net/problem/2580
import sys

board = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]
zero = []

for i in range(9):
    for j in range(9):
        if board[i][j] == 0:
            zero.append((i, j))

def check_row(y, a):
    for i in range(9):
        if a == board[y][i]:
            return False
    return True

def check_col(x, a):
    for i in range(9):
        if a == board[i][x]:
            return False
    return True

def check_3(y, x, a):
    ny = y//3*3
    nx = x//3*3

    for i in range(3):
        for j in range(3):
            if a == board[ny+i][nx+j]:
                return False
    return True

def dfs(num):
    if num == len(zero):
        for i in range(9):
            print(*board[i])
        exit(0)
    for k in range(1, 10):
        y = zero[num][0]
        x = zero[num][1]
        if check_row(y, k) and check_col(x, k) and check_3(y, x, k):
            board[y][x] = k
            dfs(num + 1)
            board[y][x] = 0

dfs(0)