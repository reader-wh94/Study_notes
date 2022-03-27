graph = dict()
 
graph['A'] = ['B', 'C']
graph['B'] = ['A', 'D']
graph['C'] = ['A', 'G', 'H', 'I']
graph['D'] = ['B', 'E', 'F']
graph['E'] = ['D']
graph['F'] = ['D']
graph['G'] = ['C']
graph['H'] = ['C']
graph['I'] = ['C', 'J']
graph['J'] = ['I']

# list 사용
def dfs_list(graph, start_node):
  
  # 항상 두개의 리스트를 별도로 관리
  need_visited, visited = list(), list()
  
  # 시작 노드 설정
  need_visited.append(start_node)
  
  # 방문이 필요한 노드가 있다면
  while need_visited:
    # 그 중에서 마지막 데이터를 추출 (스택 구조 사용)
    node = need_visited.pop()
    
    # 만약 해당 노드가 방문 목록에 없다면
    if node not in visited:
      # 방문 목록에 추가
      visited.append(node)
      
      # 그 노드에 연결된 노드를
      need_visited.extend(graph[node])
  
  return visited


# deque 사용
def dfs_deque(graph, start_node):
  # deque 패키지 
  from collections import deque
  visited = []
  need_visited = deque()
  
  # 시작 노드 설정
  need_visited.append(start_node)
  
  # 방문이 필요한 리스트가 아직 존재한다면
  while need_visited:
    # 시작 노드를 지정
    node = need_visited.popleft()
    
    # 만약 방문 리스트에 없다면
    if node not in visited:
      # 방문 리스트에 노드를 추가
      visited.append(node)
      
      # 인접 노드들을 방문 예정 리스트에 추가
      need_visited.extend(graph[node])
  
  return visited


# 재귀 함수 사용
def dfs_recursive(graph, start, visited = []):
  # 데이터를 추가하는 명령어 / 재귀가 이루어짐
  visited.append(start)
  
  for node in graph[start]:
    if node not in visited:
      dfs_recursive(graph, node, visited)
  
  return visited

print(dfs_recursive(graph, 'A'))
print(dfs_list(graph, 'A'))
print(dfs_deque(graph, 'A'))

# 출처 - https://data-marketing-bk.tistory.com/44