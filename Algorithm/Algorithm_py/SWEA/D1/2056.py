# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AV5QLkdKAz4DFAUq&categoryId=AV5QLkdKAz4DFAUq&categoryType=CODE&problemTitle=&orderBy=RECOMMEND_COUNT&selectCodeLang=PYTHON&select-1=1&pageSize=10&pageIndex=1

mon = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

N = int(input())

for i in range(N):
    s = input()
    month = int(s[4:6])
    day = int(s[6:8])
    res = -1

    if s[0:4] == '0000':
        print(f"#{i + 1} {res}")
    else:
        if 1 <= month <= 12 and 1 <= day <= mon[month - 1]:
            res = s[0:4] + '/' + s[4:6] + '/' + s[6:8]
            print(f"#{i + 1} {res}")
        else:
            print(f"#{i + 1} {res}")