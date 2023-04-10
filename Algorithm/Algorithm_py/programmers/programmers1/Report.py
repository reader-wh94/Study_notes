# https://programmers.co.kr/learn/courses/30/lessons/92334
def solution(id_list, reports, k):
  
    dic = {id: [] for id in id_list}
    answer = [0] * len(id_list)
  
    for report in set(reports):
        report = report.split(' ')
        dic[report[1]].append(report[0])
  
    for key, value in dic.items():
        if len(value) >= k:
            for v in value:
                answer[id_list.index(v)] += 1
  
    return answer