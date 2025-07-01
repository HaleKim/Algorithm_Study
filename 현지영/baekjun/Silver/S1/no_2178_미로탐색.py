from collections import deque

def bfs(x, y) :
    directions = [(-1,0), (1,0), (0,1), (0,-1)]
    queue = deque()
    queue.append((x,y))

    while queue :
        x,y = queue.popleft()

        for dx, dy in directions :
            nx, ny = x+dx, y+dy

            if 0<= nx <n and 0<= ny < m and graph[nx][ny] == 1 :
                queue.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1
    return graph[n-1][m-1]

print(bfs(0,0))