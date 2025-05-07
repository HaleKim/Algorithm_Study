s = input('현재 좌표:')

x = ord(s[0])- ord('a')
y = int(s[1])-1

# 오른쪽, 아래, 왼쪽, 위
direction = [(2,-1), (2,1),
             (1,2), (-1,2),
             (-2,-1), (-2,1),
             (1,-2), (-1,-2)]

cnt = 0
for d in direction:
    nx = x + d[0]
    ny = y + d[1]

    if 0<=nx<8 and 0<=ny<8:
        cnt += 1
print(cnt)