# https://programmers.co.kr/learn/courses/30/lessons/12932?language=python3
def solution(n):
    answer = list(map(int, str(n)))
    answer.reverse()
    return answer
