# https://programmers.co.kr/learn/courses/30/lessons/42586
def solution(progresses, speeds):
    answer = []
    days = []
    count = 0
    
    for i, v in enumerate(progresses): 
        x = (100 - v) / speeds[i]
        if x - int(x) == 0:
            days.append(int(x))
        else:
            days.append(int(x) + 1)
            
        if answer and count >= x:
            answer[-1] += 1
        else:
            count = x
            answer.append(1)
    
    return answer

# 2번 실패

def solution2(progresses, speeds):
    answer = []
    days = []
    count = 0
    
    for i, v in enumerate(progresses): 
        x = (100 - v) / speeds[i]
        if x - int(x) == 0:
            days.append(int(x))
        else:
            days.append(int(x) + 1)
        
    for i in days:
        if i > count:
            answer.append(1)
            count = i
        else:
            answer[-1] += 1

    return answer
# for문을 따로 돌렸다