# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AV5QFZtaAscDFAUq&categoryId=AV5QFZtaAscDFAUq&categoryType=CODE&problemTitle=&orderBy=RECOMMEND_COUNT&selectCodeLang=PYTHON&select-1=1&pageSize=10&pageIndex=2

N = int(input())
sum = 0

for i in range(N, 0, -1):
    sum += i

print(sum)