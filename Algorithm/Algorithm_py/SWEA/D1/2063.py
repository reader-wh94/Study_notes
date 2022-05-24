# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AV5QPsXKA2UDFAUq&categoryId=AV5QPsXKA2UDFAUq&categoryType=CODE&problemTitle=&orderBy=RECOMMEND_COUNT&selectCodeLang=PYTHON&select-1=1&pageSize=10&pageIndex=1

N = int(input())
num = list(map(int, input().split()))

num.sort()

print(num[len(num) // 2])