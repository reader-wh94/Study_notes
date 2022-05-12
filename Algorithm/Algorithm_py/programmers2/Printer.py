# https://programmers.co.kr/learn/courses/30/lessons/42587
from collections import deque

def solution(priorities, location):
    answer = 0
    queue = deque([(v, i) for i, v in enumerate(priorities)])

    while priorities:
        current = queue.popleft()
        if current[0] < max(queue)[0]:
            queue.append(current)
        else:
            answer += 1
            if current[1] == location:
                break 
    return answer
# 예시 2, 6, 18번이 오류가 나는데 왜 나는지 모르겠다

def solution2(priorities, location):
    answer = 1
    queue = deque([(v, i) for i, v in enumerate(priorities)])

    while queue:
        current = queue.popleft()
        if any(current[0] < q[0] for q in queue): 
            queue.append(current)
        else:
            if current[1] == location:
                return answer
            answer += 1 
    return answer
#any로 조건 바꿨더니 통과..
print(solution([2, 1, 3, 2], 2))