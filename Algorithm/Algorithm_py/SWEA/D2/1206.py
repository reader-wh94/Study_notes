# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&problemLevel=2&problemLevel=3&contestProbId=AV134DPqAA8CFAYh&categoryId=AV134DPqAA8CFAYh&categoryType=CODE&problemTitle=&orderBy=RECOMMEND_COUNT&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=1

t = 10

for tc in range(1, t + 1):
    N = int(input())
    buildings = list(map(int, input().split()))
    count = 0

    for i in range(2, len(buildings) - 2):
        if buildings[i] > buildings[i-1] and buildings[i] > buildings[i-2] and buildings[i] > buildings[i+1] and buildings[i] > buildings[i+2]:
            l1 = buildings[i] - buildings[i-1]
            l2 = buildings[i] - buildings[i-2]
            r1 = buildings[i] - buildings[i+1]
            r2 = buildings[i] - buildings[i+2]
            gap = l1

            for j in [l1, l2, r1, r2]:
                if j < gap:
                    gap = j
            count += gap

    print(f"#{tc} {count}")


