# https://pacific-ocean.tistory.com/148

n = int(input())
tri = [list(map(int, input().split())) for _ in range(n)]
k = 2

for i in range(1, n):
    for j in range(k):
        if j == 0:
            tri[i][j] = tri[i][j] + tri[i-1][j]
        elif j == i:
            tri[i][j] = tri[i][j] + tri[i-1][j-1]
        else:
            tri[i][j] = max(tri[i-1][j-1], tri[i-1][j]) + tri[i][j]
    k += 1

print(max(tri[n-1]))

# tri[i] 라인에서 tir[i-1] 라인의 수를 선택해야한다.