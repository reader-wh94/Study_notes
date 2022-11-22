# https://www.acmicpc.net/problem/24060
import sys
input = sys.stdin.readline

def merge_sort(arr, p, r):
    if p < r and count <= k:
        q = (p + r) // 2
        merge_sort(arr, p, q)
        merge_sort(arr, q+1, r)
        merge(a, p, q, r)

def merge(arr, p, q, r):
    global res, count
    i, j = p, q + 1
    t = 1
    temp = []

    while i <= q and j <= r:
        if(arr[i] <= arr[j]):
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j += 1
    while i <= q:
        temp.append(arr[i])
        i += 1
    while j <= r:
        temp.append(arr[j])
        j += 1

    i, t = p, 0
    while i <= r:
        arr[i] = temp[t]
        count += 1
        if count == k:
            res = arr[i]
            break
        i += 1
        t += 1

n, k = map(int, input().split())
a = list(map(int, input().split()))
count, res = 0, -1
merge_sort(a, 0, n-1)
print(res)