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
def bfs_list(graph, start_node):
  need_visited, visited = [], []
  need_visited.append(start_node)
  
  while need_visited:
    node = need_visited[0]
    del need_visited[0]
    
    if node not in visited:
      visited.append(node)
      need_visited.extend(graph[node])
  return visited

# deque 사용
def bfs_deque(graph, start):
  from collections import deque
  
  visited = []
  need_visited = deque([start])

  
  # 큐가 빌 때까지 반복
  while need_visited:
    node = need_visited.popleft()

    if node not in visited:
      visited.append(node)
      need_visited.extend(graph[node])
      
  return visited

print(bfs_list(graph, 'A'))
print(bfs_deque(graph, 'A'))

# 출처 1 - https://data-marketing-bk.tistory.com/45?category=901221
# 출처 2 - https://brownbears.tistory.com/556