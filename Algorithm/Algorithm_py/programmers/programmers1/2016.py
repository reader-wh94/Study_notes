# https://programmers.co.kr/learn/courses/30/lessons/12901?language=python3
import datetime
days = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']

def solution(a, b):
    answer = days[datetime.date(2016, a, b).weekday()]
    return answer
