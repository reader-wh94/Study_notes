# https://programmers.co.kr/learn/courses/30/lessons/43165
def solution(numbers, target):
    super_node = [0]
    
    for number in numbers:
        sub_node = []
        for sup in super_node:
            sub_node.append(sup + number)
            sub_node.append(sup - number)
        super_node = sub_node

    return super_node.count(target)
# bfs와 dfs 둘 다 가능하지만 처음에는 dfs만 가능하다고 생각했다.
# dfs인건 알겠고, 어떻게 구현해야할지 모르겠어서 구글링 했다...

# https://heytech.tistory.com/141