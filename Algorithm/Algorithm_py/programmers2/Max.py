# https://programmers.co.kr/learn/courses/30/lessons/42746
def solution(numbers):
  answer = ''
  numbers_str = list(map(str, numbers))
  numbers_str.sort(key=lambda x: x*3, reverse=True)
  answer = str(int(''.join(s for s in numbers_str)))
  
  return answer

# 배열에 들어있는 값들 중에서 맨 앞자리 > 그 뒷자리 등등 비교해서
# 정렬 후 그대로 더하기..?
# 숫자마다 길이가 다 다른데 그건 어떻게 정렬하지

# 문자열 내림차순으로 정렬 > 그래야 앞자리 제일 큰 것부터 정렬이 되니까
# numbers의 원소는 0이상 1000 이하니까 문자열 각 원소에 3을 곱하기 (ex. 34, 3, 30 > 343434, 333, 303030)
# 리스트 각 요소들을 *3 하고 정렬하는 방법 > 람다 사용
# https://velog.io/@younge/Python-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EA%B0%80%EC%9E%A5-%ED%81%B0-%EC%88%98-%EC%A0%95%EB%A0%AC