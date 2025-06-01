# def dfs(start) :
#   connected = False
#   if not visited[start] :
#     visited[start] = True
#     connected = True
#     for info in node_info[start] :
#       dfs(info)
#   return connected
# recursionError 발생 => bfs로 구현

from collections import deque

def bfs(start) :
  connected = False
  queue = deque()
  if not visited[start] :
    connected = True
    visited[start] = True
    queue.append(node_info[start])
    while queue :
      for info in queue.popleft() :
        if not visited[info] :
          visited[info] = True
          queue.append(node_info[info])
  return connected

n, m = map(int,input().split())
lines = []
for _ in range(m) :
  lines.append(list(map(int, input().split())))

node_info = [[] for _ in range(n+1)]

for line in lines :
  node_info[line[0]].append(line[1])
  node_info[line[1]].append(line[0])

for i in range(1,len(node_info)) :
  node_info[i].sort()

visited = [False]*(n+1) # visited의 상태를 유지시키기 위해 외부에서 정의
answer = 0

for node in range(1,n+1) :
  answer += 1 if bfs(node) else 0

print(answer)

# 시간 초과...