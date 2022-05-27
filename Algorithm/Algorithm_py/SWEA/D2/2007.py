# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5P1kNKAl8DFAUq&categoryId=AV5P1kNKAl8DFAUq&categoryType=CODE&problemTitle=&orderBy=RECOMMEND_COUNT&selectCodeLang=PYTHON&select-1=2&pageSize=10&pageIndex=1
from collections import Counter

T = int(input())

for tc in range(1, T+1):
    s = str(input())

    for i in range(1, 10):
        if s[:i] == s[i:2*i]:
            print(f"#{tc} {i}")
            break
