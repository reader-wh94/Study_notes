# https://www.acmicpc.net/problem/1037

n = int(input())
numbers = list(map(int, input().split()))
numbers.sort()

print(numbers[0] * numbers[n-1])

# max_n = max(numbers)
# min_n = min(numbers)
#
# print(max_n * min_n)