n = int(input('입력:'))

no3_m_s= 0 # 3이 안 들어간 분, 초
for i in range(60):
    if '3' not in str(i):
        no3_m_s += 1

no3_h = 0 # 3이 안 들어간 시
for i in range(n+1):
    if '3' not in str(i):
        no3_h += 1 

print((n+1)*60*60 - no3_h * no3_m_s * no3_m_s)

def dongbin(n):
    cnt = 0
    for h in range(n+1):
        for m in range(60):
            for s in range(60):
                time = str(h) + str(m) + str(s)
                if '3' in time:
                    cnt += 1
    return cnt