# https://www.acmicpc.net/problem/11478

s = input()
text = set()

for i in range(len(s)):
    for j in range(i, len(s)):
        text.add(s[i:j+1])
print(len(text))