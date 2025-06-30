

# 내가 작성한 graph 만드는 코드 ->  에러...
# N, M, V = input().split()
# nums = [input().split() for _ in range(int(M))]
# keys = list(range(int(N)+1))
# graph = {k: [] for k in keys}
# print(graph)
# for n in nums :
#     graph[int(n[0])].append(int(n[1]))
#     graph[int(n[1])].append(int(n[0]))

# DFS
def dfs(n) :
    visited[n] = True
    print(n, end=' ')
    for i in graph[n] :
        if not visited[i]:
            dfs(i) 

# BFS
from collections import deque
def bfs(n) :
    visited[n] = True
    queue = deque([n])

    while queue :           # 큐가 빌 때까지 반복
        q = queue.popleft() # 큐에서 하나의 원소를 뽑아 출력
        print(q, end=' ')
        for i in graph[q]:  # 해당 원소와 연결되, 아직 방문하지 않은 원소들을 큐에 삽입
            if not visited[i]:
                queue.append(i)
                visited[i] = True

N, M, V = map(int, input().split())

graph = [[]*(N+1)for _ in range(N+1)]
for i in range(M) :
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()

visited = [False] * (N+1)
dfs(V)
print()
visited = [False] * (N+1)
bfs(V)
