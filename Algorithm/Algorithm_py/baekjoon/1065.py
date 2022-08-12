# https://www.acmicpc.net/problem/1065

num = int(input())

def findHansu(num):
    hansu = 0

    for i in range(1, num+1):
        nums = list(map(int, str(i)))
        if i < 100:
            hansu += 1
        elif nums[0] - nums[1] == nums[1] - nums[2]:
            hansu += 1
    return hansu

print(findHansu(num))
