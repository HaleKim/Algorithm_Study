def dfs(c):
    ans_dfs.append(c) # 방문 노드 추가
    v[c] = 1          # 방문 표시

    for i in adj[c]:
        if not v[i]:  # 방문하지 않은 노드인 경우
            dfs(i)    # 재귀함수

def bfs(s):
    q = []            # 필요한 q, v[], 변수 생성
    q.append(s)       # Q에 초기데이터 삽입
    ans_bfs.append(s)
    v[s] = 1

    while q:
        c = q.pop(0)
        for i in adj[c]:
            if not v[i]: # 방문하지 않은 노드면 q에 삽입
                q.append(i)
                ans_bfs.append(i)
                v[i] = 1

N, M, V = map(int, input().split())
adj = [[] for _ in range(N+1)]
for _ in range(M):
    s, e = map(int, input().split())
    adj[s].append(e)
    adj[e].append(s)    # 양방향

# 1. 오름차순 정렬
for i in range(1, N+1):
    adj[i].sort()

v = [0]*(N+1)
ans_dfs = []
dfs(V)

v = [0]*(N+1)
ans_bfs = []
bfs(V)

print(*ans_dfs)
print(*ans_bfs)