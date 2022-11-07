n = int(input())
numbers = []

for _ in range(n):
    numbers.append(int(input()))

numbers = list(set(numbers))
numbers.sort()

for i in numbers:
    print(i)