# https://programmers.co.kr/learn/courses/30/lessons/64065
def solution(s):
    answer = []
    s = s[2:-2]
    s = sorted(s.split('},{'), key = lambda x: len(x))
    
    for i in s:
        x = i.split(',')
        for j in x:
            if int(j) not in answer:
                answer.append(int(j))

    return answer
  
solution('{{4,2,3},{3},{2,3,4,1},{2,3}}')