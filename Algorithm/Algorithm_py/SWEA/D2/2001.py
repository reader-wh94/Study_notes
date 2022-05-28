# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5PzOCKAigDFAUq&categoryId=AV5PzOCKAigDFAUq&categoryType=CODE&problemTitle=&orderBy=RECOMMEND_COUNT&selectCodeLang=PYTHON&select-1=2&pageSize=10&pageIndex=1

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(N)]
    flies = []

    for i in range(N - M + 1):
        for j in range(N - M + 1):
            kill = 0
            for k in range(M):
                for l in range(M):
                    kill += graph[i+k][j+l]
            flies.append(kill)

    print(f"#{tc} {max(flies)}")



