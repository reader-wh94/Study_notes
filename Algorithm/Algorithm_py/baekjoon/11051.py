# https://www.acmicpc.net/problem/11051
from math import factorial

n, k = map(int, input().split())

def binomal(n, k):
    return factorial(n) // factorial(k) // factorial(n-k)

print(binomal(n,k) % 10007)