# https://www.acmicpc.net/problem/10818

n = int(input())
numbers = list(map(int, input().split()))
max_num = numbers[0]
min_num = numbers[0]

for i in numbers[1:]:
    if i > max_num:
        max_num = i
    elif i < min_num:
        min_num = i

print(min_num, max_num)

# print(min(numbers), max(numbers))
