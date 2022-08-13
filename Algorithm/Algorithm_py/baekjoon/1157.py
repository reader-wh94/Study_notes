# https://www.acmicpc.net/problem/1157

s = input().upper()
word_list = list(set(s))
count_list = [s.count(i) for i in word_list]

if count_list.count(max(count_list)) > 1:
    print('?')
else:
    print(word_list[count_list.index(max(count_list))])