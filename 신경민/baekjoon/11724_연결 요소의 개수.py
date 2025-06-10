def dfs(c):
    v[c] = 1
    for i in adj[c]:
        if not v[i]:
            dfs(i)  

N, M= map(int, input().split())
adj = [[] for _ in range(N+1)]
for _ in range(M):
    s, e = map(int, input().split())
    adj[s].append(e)

v = [0]*(N+1)

count = 0
for i in range(1, N+1):
    if not v[i]:
        dfs(i)
        count += 1

print(count)