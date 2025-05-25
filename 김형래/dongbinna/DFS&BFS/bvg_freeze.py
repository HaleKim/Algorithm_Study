from collections import deque

n, m = map(int,input().split())

box = []
for _ in range(n) :
  box.append(list(map(int,input())))
answer = 0

# visited = [False]*(n*m)
# stack = []
# dx = [1,-1,0,0]
# dy = [0,0,1,-1]

# def dfs(graph, start, visited) :

# for i in range(n) :
#   for j in range(m) :
#     now = box[i][j]
#     if now == 0 :
#       stack.append(box[i][j])
#       visited[i][j] = True
'''
강의의 예시 코드에만 맞춰 생각하지 말자!
여기에선 방문했는지 여부를 새로운 컨테이너에 저장하는것이 아닌 입력받은
컨테이너 자체를 변경하는 것으로 대체한 등의 차이점이 존재한다.
또한 1을 만나면 방문한 노드로 판별하는 등의 조건의 차별점도 존재하므로,
여러 문제를 풀어보며 경험을 쌓는 것이 중요해보인다.
'''

# def dfs(x,y) :
#   if x < 0 or x >= n or y < 0 or y >= m : # 범위를 벗어난 경우
#     return False
#   elif box[x][y] == 0 : # 현재 위치가 방문하지 않은 위치일때
#     box[x][y] = 1 # 방문 표시
#     dfs(x-1,y) # 상하좌우도 방문
#     dfs(x+1,y)
#     dfs(x,y-1)
#     dfs(x,y+1)
#     return True # 방문하지 않은 위치에 접근했다면 무조건 True 반환
#   return False # 방문했던 곳이면(1이면) false 반환

# # 모든 노드를 start로 설정하여 dfs 수행
# for i in range(n) :
#   for j in range(m) :
#     if dfs(i,j) :
#       answer += 1

# print(answer)

# ---- bfs로 풀어보기

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y) :
  isice = False
  queue = deque()
  queue.append((x,y))

  while queue :
    x,y = queue.popleft()
    for i in range(4) :
      nx = x + dx[i]
      ny = y + dy[i]
      if nx < 0 or nx >= n or ny < 0 or ny >= m :
        continue
      elif box[nx][ny] == 1:
        continue
      else :
        isice = True
        box[nx][ny] = 1
        queue.append((nx,ny))
  return isice

for i in range(n) :
  for j in range(m) :
    if bfs(i,j) :
      answer += 1

print(answer)