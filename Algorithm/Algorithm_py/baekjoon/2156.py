# https://www.acmicpc.net/problem/2156

n = int(input())
wine = [0] * 10002
dp = [0] * 10002

for i in range(1, n+1):
    wine[i] = int(input())

dp[1] = wine[1]
dp[2] = wine[1] + wine[2]

for i in range(3, n+1):
    dp[i] = max(dp[i-1], dp[i-3] + wine[i-1] + wine[i], dp[i-2] + wine[i])
    # dp[i-1]잔만 마시고 이번 잔은 안마시는 경우
    # 이번 잔과 wine[i-1]잔을 마셨을 때 그 전에 마신 잔은 dp[i-3]잔 인 경우
    # 이번 잔과 전전 잔을 마신 경우
print(dp[n])

