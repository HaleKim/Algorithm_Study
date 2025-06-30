# 기본 뻔 데기 뻔 데기
front = [0,1,0,1]

# 인원수에 따른 몇번을 돌린건지
a = int(input())
t  = int(input())
bd = int(input())
p = a
c = 0 # 번데기 몇번나와야하는지 확인
round = 2 # 번번데기데기 번번번데기데기데기  이걸 위한 라운드
cnt=0 # 번데기 노래 돌림을 몇번해야하는지 위한 카운트
while True:
    c += round
    round+=1
    cnt+=1
    if c >=t:
        break

# 위에서 몇번 돌린지에 따른 뻔데기 돌림판
back = []
for i in range(cnt):
    back += front + [0]*(i+2) + [1]*(i+2)

answer = [i for i in range(p)]
count = 0
for i in range(len(back)):
    if back[i] == bd:
        count+=1
        if count == t:
            print(answer[(i % p)])
            break