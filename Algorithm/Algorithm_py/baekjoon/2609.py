# https://www.acmicpc.net/problem/2609
import math

a, b = map(int, input().split())

print(math.gcd(a, b))
print(math.lcm(a, b))