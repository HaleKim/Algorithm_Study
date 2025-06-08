# def dfs(start) :
#   connected = False
#   if not visited[start] :
#     visited[start] = True
#     connected = True
#     for info in node_info[start] :
#       dfs(info)
#   return connected
# recursionError 발생 => bfs로 구현

# from collections import deque

# def bfs(start) :
#   connected = False
#   queue = deque()
#   if not visited[start] :
#     connected = True
#     visited[start] = True
#     queue.append(node_info[start])
#     while queue :
#       for info in queue.popleft() :
#         if not visited[info] :
#           visited[info] = True
#           queue.append(node_info[info])
#   return connected

# n, m = map(int,input().split())
# lines = []
# for _ in range(m) :
#   lines.append(list(map(int, input().split())))

# node_info = [[] for _ in range(n+1)]

# for line in lines :
#   node_info[line[0]].append(line[1])
#   node_info[line[1]].append(line[0])

# for i in range(1,len(node_info)) :
#   node_info[i].sort()

# visited = [False]*(n+1) # visited의 상태를 유지시키기 위해 외부에서 정의
# answer = 0

# for node in range(1,n+1) :
#   answer += 1 if bfs(node) else 0

# print(answer)

# 시간 초과..
# ------------------------------------------------------------
# 입력 방식 수정
# queue에 append하는 값 수정
# connected flag 제거
# 입력 방식 변경
# ------------------------------------------------------------

from collections import deque
import sys

def bfs(start):
    if visited[start]: 
        return False
    
    queue = deque([start]) # queue에 리스트 전체를 저장하지 않고, 노드 자체를 저장함
    visited[start] = True
    
    while queue:
        current = queue.popleft()  # 현재 노드만 꺼냄
        for neighbor in node_info[current]:  # 인접 노드 순회
            if not visited[neighbor]:
                visited[neighbor] = True  # 방문 즉시 처리
                queue.append(neighbor)
    return True  # 새로운 연결 요소 발견

n, m = map(int, sys.stdin.readline().split())
node_info = [[] for _ in range(n+1)]

# 그래프 구성 (간선 정보 처리)
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    node_info[a].append(b)
    node_info[b].append(a)

visited = [False] * (n+1)
answer = 0

# 모든 노드 순회하며 연결 요소 카운트
for node in range(1, n+1):
    if bfs(node):
        answer += 1

print(answer)