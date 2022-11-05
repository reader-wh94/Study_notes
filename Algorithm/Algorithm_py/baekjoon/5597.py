# https://www.acmicpc.net/problem/5597

a = [i for i in range(1, 31)]
b = []

for i in range(28):
    b.append(int(input()))

none = []
for i in a:
    if i not in b:
        none.append(i)

print(min(none))
print(max(none))