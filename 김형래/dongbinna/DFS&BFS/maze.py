from collections import deque

n, m = map(int, input().split())

maze = []
for _ in range(n) :
  maze.append(list(map(int, input())))

dx = [1,0,-1,0]
dy = [0,1,0,-1]
# 하우상좌 >> 출구와 가까운 부분부터 이동하는게 좋아보여서..

def bfs(x,y) :
  queue = deque()
  queue.append((x,y))

  while queue :
    x,y = queue.popleft()
    for i in range(4) :
      nx = x + dx[i]
      ny = y + dy[i]

      if nx < 0 or nx >= n or ny < 0 or ny >= m :
        continue
      elif maze[nx][ny] != 1 :
        continue
      else :
        maze[nx][ny] = maze[x][y] + 1
        queue.append((nx,ny))

bfs(0,0)
print(maze[n-1][m-1])