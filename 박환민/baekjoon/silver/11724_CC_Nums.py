import sys
input = sys.stdin.readline  # 런타임에러 해결

N,M = map(int, input().split())

graph = [[] for _ in range(N+1)]

for i in range(M) :
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


visited = [False] * (N+1)
cnt = 0

# 재귀함수 대신 for문 사용
# DFS니깐 끊기지 않게 모든 노드를 순회해야함 > 하나의 요소만 탐색하지 않기 위해서
for start in range(1, N+1):
    if not visited[start]:
        cnt += 1 # 스택이 비어서 다시 돌아왔을 때, 연결요소를 +1 해줌
        # 스택을 이용한 반복문 DFS
        stack = [start]
        visited[start] = True

        while stack:
            node = stack.pop()
            for nxt in graph[node]:
                if not visited[nxt]:
                    visited[nxt] = True
                    stack.append(nxt)

print(cnt)