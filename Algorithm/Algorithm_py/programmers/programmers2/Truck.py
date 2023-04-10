# https://programmers.co.kr/learn/courses/30/lessons/42583
def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge_truck = [0] * bridge_length
    
    while len(bridge_truck) != 0:
        answer += 1
        bridge_truck.pop(0)
        if truck_weights:
            if sum(bridge_truck) + truck_weights[0] <= weight:
                bridge_truck.append(truck_weights.pop(0))
            else:
                bridge_truck.append(0)
    
    return answer

solution(2, 10, [7,4,5,6])