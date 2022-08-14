# https://www.acmicpc.net/problem/5622

list = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
word = input()
time = 0

for i in list:
    for j in i:
        for k in word:
            if j == k:
                time += list.index(i) + 3

print(time)