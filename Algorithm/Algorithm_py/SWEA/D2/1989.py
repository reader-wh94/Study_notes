# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5PyTLqAf4DFAUq&categoryId=AV5PyTLqAf4DFAUq&categoryType=CODE&problemTitle=&orderBy=RECOMMEND_COUNT&selectCodeLang=PYTHON&select-1=2&pageSize=10&pageIndex=2

T = int(input())

for tc in range(1, T+1):
    s = input()
    reverse_s = s[::-1]

    if s == reverse_s:
        print(f"#{tc} {1}")
    else:
        print(f"#{tc} {0}")