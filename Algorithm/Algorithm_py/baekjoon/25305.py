# https://www.acmicpc.net/problem/25305

n, k = map(int, input().split())
scores = list(map(int, input().split()))

scores.sort(reverse=True)
print(scores[k-1])