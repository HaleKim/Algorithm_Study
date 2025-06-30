# 연결 요소의 개수
# 방향 없는 그래프가 주어졌을 때, 
# 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.
# M개의 줄에 간선의 양 끝점 u와 v가 주어진다. (1 ≤ u, v ≤ N, u ≠ v) 같은 간선은 한 번만 주어진다.
# 첫째 줄에 연결 요소의 개수를 출력한다.

# dfs 또는 bfs를 수행하는 횟수 : 연결 요소의 개수


import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[]*(N+1)for _ in range(N+1)]
for i in range(M) :
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()


# 1 DFS 이용
# dfs 함수
def dfs(graph, v, visited) :
    visited[v] = True
    for i in graph[v] :
        if not visited[i]:
            dfs(graph, i, visited)

count = 0 # 연결 노드의 수
visited = [False] * (N+1)
for i in range(1,N+1) :
    if not visited[i]:
        dfs(graph, i, visited)
        count += 1
print(count)


# 2. BFS 이용
# bfs 함수
from collections import deque
def bfs(graph, start, visited) :
    queue = deque([start])
    visited(start) = True

    while queue:
        v = queue.popleft()
        for i in graph[v] :
            if not visited[v] :
                queue.append(i)
                visited[i] = True

count = 0 # 연결 노드의 수
visited = [False] * (N+1)
for i in range(1,N+1) :
    if not visited[i]:
        bfs(graph, i, visited)
        count += 1
print(count)
