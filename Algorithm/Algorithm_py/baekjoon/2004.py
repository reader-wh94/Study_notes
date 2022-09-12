# https://www.acmicpc.net/problem/2004

n, m = map(int, input().split())

def count_two(n):
    count = 0
    while n != 0:
        n //= 2
        count += n
    return count

def count_five(n):
    count = 0
    while n != 0:
        n //= 5
        count += n
    return count

if m == 0:
    print(0)
else:
    print(min(count_two(n) - count_two(m) - count_two(n - m), count_five(n) - count_five(m) - count_five(n -m)))