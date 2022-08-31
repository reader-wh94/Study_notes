# https://www.acmicpc.net/problem/18870

n = int(input())
numbers = list(map(int, input().split()))
num_dic = {}

numbers_set = sorted(set(numbers))

for i in range(len(numbers_set)):
    num_dic[numbers_set[i]] = i

for i in numbers:
    print(num_dic[i], end=' ')