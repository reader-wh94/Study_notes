# https://www.acmicpc.net/problem/1018

n, m = map(int, input().split())
board = []
min_list = []

for i in range(n):
    a = input()
    board.append(a)

for i in range(n-7):
    for j in range(m-7):
        num1, num2 = 0, 0

        for a in range(i, i+8):
            for b in range(j, j+8):
                if (a+b) % 2 == 0:
                    if board[a][b] != 'W':
                        num1 += 1
                    else:
                        num2 += 1
                else:
                    if board[a][b] != 'B':
                        num1 += 1
                    else:
                        num2 += 1

        min_list.append(num1)
        min_list.append(num2)

print(min(min_list))