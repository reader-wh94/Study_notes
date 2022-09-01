# https://www.acmicpc.net/problem/10815
import sys

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

n = int(sys.stdin.readline())
n_number = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
m_number = list(map(int, sys.stdin.readline().split()))

n_number.sort()

for i in m_number:
    if binary_search(n_number, i, 0, n-1) is not None:
        print("1", end=' ')
    else:
        print("0", end=' ')
