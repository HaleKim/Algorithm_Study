import sys

a = int(input())
t = int(input())
opt = int(input())

occ = 0   
idx = 0  

k = 1
while True:
    # 문장 앞부분: 뻔–데기–뻔–데기 고정
    for ch in (0, 1, 0, 1):
        if ch == opt:
            occ += 1
            if occ == t:
                print(idx % a)
                sys.exit()
        idx += 1
    
    for _ in range(k + 1):
        if opt == 0:
            occ += 1
            if occ == t:
                print(idx % a)
                sys.exit()
        idx += 1

    for _ in range(k+1):
        if opt == 1:
            occ += 1
            if occ == t:
                print(idx % a)
                sys.exit()
        idx += 1
    
    k += 1
    