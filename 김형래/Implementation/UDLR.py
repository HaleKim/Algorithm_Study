n = int(input())
plan = input().split()

move = {'U':(-1,0), 'D':(1,0), 'L':(0,-1), 'R':(0,1)}
now = [1,1]

for dir in plan :
    dx, dy = move[dir]
    
    now[0] += dx
    now[1] += dy

    if now[0] < 1 or now[0] > n :
        now[0] -= dx
    elif now[1] < 1 or now[1] > n :
        now[1] -= dy

    print(now)

print("%d %d" % (now[0], now[1]))

# 쓸데없는 -연산 수행하는거보다 nx, ny 만들어두고 좌표에 더할지 말지 조건문으로 결정하는게 나아보인다!