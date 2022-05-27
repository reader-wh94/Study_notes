# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&problemLevel=3&contestProbId=AV5PobmqAPoDFAUq&categoryId=AV5PobmqAPoDFAUq&categoryType=CODE&problemTitle=&orderBy=RECOMMEND_COUNT&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=1

T = int(input())

for tc in range(1, T + 1):
    n = int(input())

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    snail = [[0]*n for _ in range(n)]
    dist, x, y = 0, 0, 0 # 방향, x,y좌표

    for i in range(1, n**2+1):
        snail[x][y] = i
        x += dx[dist]
        y += dy[dist]

        if x < 0 or y < 0 or x >= n or y >= n or snail[x][y] != 0:
            x -= dx[dist]
            y -= dy[dist]

            dist = (dist+1)%4

            x += dx[dist]
            y += dy[dist]

    print(f"#{tc}")
    for arr in snail:
        for num in arr:
            print(num, end=' ')
        print()
