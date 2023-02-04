# https://www.acmicpc.net/problem/14889
import sys
input = sys.stdin.readline

def dfs(idx):
    global res

    if idx == n // 2:
        s_res, l_res = 0, 0
        for i in range(0, n):
            if i not in st:
                li.append(i)
        for i in range(0, n // 2 - 1):
            for j in range(i+1, n // 2):
                s_res += arr[st[i]][st[j]] + arr[st[j]][st[i]]
                l_res += arr[li[i]][li[j]] + arr[li[j]][li[i]]

        char = abs(s_res - l_res)
        if res > char:
            res = char
        li.clear()
        return

    for i in range(n):
        if i in st:
            continue
        if len(st) > 0 and st[len(st) - 1] > i:
            continue
        st.append(i)
        dfs(idx + 1)
        st.pop()

n = int(input())
arr = []
st = []
li = []
for i in range(n):
    arr.append(list(map(int, input().split())))

res = int(1e9)
dfs(0)
print(res)