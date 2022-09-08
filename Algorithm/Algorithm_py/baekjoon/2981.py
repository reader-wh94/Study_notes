# https://www.acmicpc.net/problem/2981
import sys
from math import gcd

n = int(sys.stdin.readline())
m_list = [int(sys.stdin.readline()) for _ in range(n)]
m_list.sort()

temp = [m_list[i] - m_list[i-1] for i in range(1, n)]
my_gcd = temp[0]

for i in range(1, n-1):
    my_gcd = gcd(my_gcd, temp[i])

res = []
for i in range(1, int(my_gcd ** 0.5) + 1):
    if my_gcd % i == 0:
        if i ** 2 == my_gcd:
            res.append(i)
        else:
            res += [i, my_gcd // i]

res.remove(1)
res.sort()

for i in range(len(res)):
    print(res[i], end=" ")