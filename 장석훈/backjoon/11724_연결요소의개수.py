#DFS.깊이우선 count+1 ->연결요소의 개수를 구할 수 있음
import sys
input = sys.stdin.readline

node, edge = map(int, input().split())
# 그래프
graph = [[] for _ in range(node+1)]

# 방문 여부 표시
visited = [False] * (node + 1)

for i in range(edge):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

stack = []

def dfs(new):
    while stack:
        n = stack.pop()
        if not visited[n]:
            for i in graph[n]:
                stack.append(i)
            visited[n] = True

cnt = 0
##
for test in range(1, node+1):
    if not visited[test]:
        stack.append(test)
        dfs(test)
        # 만약 이전에 방문했다면 하나의 연결 노드였을 것이다.
        cnt += 1

print(cnt)