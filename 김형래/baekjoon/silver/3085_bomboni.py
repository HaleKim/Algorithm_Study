# row, col 에서 가장 많은 놈의 개수 구하는 방법? => 그냥 분해해서 count 사용..
# 단순 개수 구하는게 아니라 연속되는 놈들의 개수 구하기!
# [N,:] 슬라이싱은 ndarray에서만 제공 => comprehension 사용
# 2차원 배열 인덱스로 접근 시 i,j 인덱스 바꾸며 접근하는 idea 기억!

import sys

n = int(sys.stdin.readline())
board = []
for _ in range(n) :
  board.append(list(sys.stdin.readline().strip()))

answer = 0

def rowcolMax() :
  maxCnt = 1
  for i in range(n) :
    cnt = 1
    for j in range(1,n) :
      if board[i][j] == board[i][j-1] : cnt += 1
      else : cnt = 1
      maxCnt = max(cnt, maxCnt)

    cnt = 1
    for j in range(1,n) :
      if board[j][i] == board[j-1][i] : cnt += 1
      else : cnt = 1
      maxCnt = max(cnt, maxCnt)

  return maxCnt

for i in range(n) :
  for j in range(n) :
    if j+1 < n : # 가로 swap
      board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
      answer = max(answer,rowcolMax())
      board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
    if i+1 < n : # 세로 swap
      count_list = [0,0,0,0]
      board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
      answer = max(answer,rowcolMax())
      board[i][j], board[i+1][j] = board[i+1][j], board[i][j]

print(answer)

# colors = ['C','P','Z','Y']

# for i in range(n) : # 원상태일때 max check
#   col = [row[i] for row in board]
#   for color in colors : 
#     if max < board[i].count(color) : # 가로 max check
#       max = board[i].count(color)
#     if max < col.count(color) : # 세로 max check
#       max = col.count(color)

# for i in range(n) :
#   for j in range(n) :
#     if j+1 < n : # 가로 swap
#       board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
#       col = [row[j] for row in board]
#       for color in colors : 
#         if max < board[i].count(color) : # 가로 max check
#           max = board[i].count(color)
#         if max < col.count(color) : # 세로 max check
#           max = col.count(color)
#       board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
      
#     if i+1 < n : # 세로 swap
#       board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
#       col = [row[j] for row in board]
#       for color in colors : 
#         if max < board[i].count(color) : # 가로 max check
#           max = board[i].count(color)
#         if max < col.count(color) : # 세로 max check
#           max = col.count(color)
#       board[i][j], board[i+1][j] = board[i+1][j], board[i][j]