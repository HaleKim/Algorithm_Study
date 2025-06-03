from collections import deque

def dfs(v) :
  if not visited[v] :
    print(v, end=' ')
    visited[v] = True
    for dest in node_info[v] :
      dfs(dest)

def bfs(v) :
  queue = deque()
  visited = [False]*(n+1)

  print(v, end=' ')
  visited[v] = True
  queue.append(node_info[v])
  while queue :
    for info in queue.popleft() :
      if not visited[info] :
        print(info, end=' ')
        visited[info] = True
        queue.append(node_info[info])

n, m, v = map(int, input().split())
lines = []
for _ in range(m) :
  lines.append(list(map(int, input().split())))

node_info = [[] for _ in range(n+1)]

for line in lines :
  node_info[line[0]].append(line[1])
  node_info[line[1]].append(line[0])

for i in range(1,len(node_info)) :
  node_info[i].sort()

visited = [False]*(n+1)

dfs(v)
print()
bfs(v)