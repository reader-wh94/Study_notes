# https://www.acmicpc.net/problem/3052

numbers = [int(input()) for _ in range(10)]
new_numbers = []

for i in numbers:
    new_numbers.append(i % 42)

new_numbers = set(new_numbers)
print(len(new_numbers))

