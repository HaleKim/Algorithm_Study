from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]

def bfs(x,y) :
    directions = [(1,0), (-1,0), (0,1), (0,-1)]
    queue = deque()
    queue.append((x,y))

    while queue : 
        x, y = queue.popleft()
        for dx, dy in directions :
            nx, ny = x+dx, y+dy
            if 0<=nx<m+1 and 0<=ny<n+1 and graph[nx][ny]==1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))
    return graph[n-1][m-1]

print(bfs(0,0))