# https://www.acmicpc.net/problem/1427

number = list(map(int, str(input())))
number.sort(reverse=True)

print(''.join(map(str, number)))