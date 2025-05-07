n = int(input('공간 크기: '))
plan = list(input('계획서: ').split())

#   오른쪽 아래 왼쪽 위
direction = {'R': (0, 1),
             'U': (-1, 0),
             'L': (0, -1),
             'D': (1, 0)}


me = [1, 1]
for p in plan:
    x, y = direction[p]
    nx = me[0] + x
    ny = me[1] + y

    if 0 < nx <= n and 0 < ny <= n:
        me  = [nx, ny]

print(me)