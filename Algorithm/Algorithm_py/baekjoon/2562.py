# https://www.acmicpc.net/problem/2562

numbers = [int(input()) for _ in range(9)]
max = max(numbers)

print(max)
print(numbers.index(max))