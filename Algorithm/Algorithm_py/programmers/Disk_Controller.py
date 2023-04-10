import heapq

def solution(jobs):
    answer, time, check = 0, 0, 0
    start = -1
    heap = []

    while check < len(jobs):
        # 현재 시점에서 처리할 수 있는 작업을 heap에 저장
        for j in jobs:
            if start < j[0] <= time:
                heapq.heappush(heap, [j[1], j[0]])

        if len(heap) > 0: # 처리할 작업이 있는 경우
            now = heapq.heappop(heap)
            start = time
            time += now[0]
            answer += (time - now[1]) # 작업 요청 시간부터 종료 시간까지의 시간 계산
            check += 1
        else: # 처리할 작업이 없는 경우 다음 시간으로 넘어감
            time += 1

    return int(answer / len(jobs))