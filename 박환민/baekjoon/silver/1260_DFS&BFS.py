# DFS는 깊이우선탐색 > 선입후출 > 스택사용
# BFS는 너비우선탐색 > 선입선출 > 큐 사용
from collections import deque

N, M, V = map(int, input().split())

# 그래프 그려주기
graph = [[] for _ in range(N+1)] # 이중리스트 초기화 > 처음에 빈 리스트 추가 위해 N+1

for i in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u) # 양방향 이니깐

for i in graph :
    i.sort()

def dfs(graph, V, visited):
    visited[V] = True
    print(V, end=' ')

    for i in graph[V] :
        if not visited[i] :
            dfs(graph, i, visited) # 스택대신 재귀함수 사용 > for문 안의 재귀함수이므로 stack처럼 선입후출이됨(깊이있게 탐색)

def bfs(graph, start, visited2):
    queue = deque([start])
    visited2[start] = True
    while queue :
        V = queue.popleft()
        print(V, end=' ')
        for i in graph[V]:
            if not visited2[i]:
                queue.append(i) # 큐는 일단 다 넣음 > 재귀함수를 사용하지 않음(BFS와의 차이점)
                visited2[i] = True

visited = [False] * (N+1)
visited2 = [False] * (N+1)
dfs(graph, V, visited)
print()
bfs(graph, V, visited2)
