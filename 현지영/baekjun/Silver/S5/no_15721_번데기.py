A = int(input())  # 게임 하는 사람 수 <= 2000
T = int(input())  # 구하고자하는 번째 <= 10000
g = int(input())  # 뻔=0 / 데기=1

b = 0
d = 0 

cnt = 0
N = []

while True :
    cnt += 1
    for _ in range(2) :
        b += 1
        N.append((0,b))
        d += 1
        N.append((1,d))
    for _ in range(cnt+1) :
        b += 1
        N.append((0,b))
    for _ in range(cnt+1) :
        d += 1
        N.append((1,d))
    
    if b >= T :
        print(N.index((g,T))%A)
        break
