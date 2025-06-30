# 시작시간, 간격, 대수
# 영식 T분에 버스터미널 도착 
# 버스 타려면 최소 몇분을 기다려야 하는지

# N(버스의 개수) T(버스터미널 도착시간)
# S(버스의 시작시간) I(간격) C(대수)

N, T = map(int, input().split())
bus = []
for _ in range(N) :
    S, I, C = map(int, input().split())
    for num in range(C):
        bus.append(S+I*num)

s_bus = sorted(bus)
if T > s_bus[-1] :
    print(-1)
else :
    for b in s_bus :
        if b-T >= 0:
            print(b-T)
            break
