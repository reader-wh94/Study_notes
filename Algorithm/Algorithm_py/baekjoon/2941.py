# https://www.acmicpc.net/problem/2941

list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()

for i in list:
    word = word.replace(i, '*')

print(len(word))