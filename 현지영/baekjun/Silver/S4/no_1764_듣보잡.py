# 리스트에 append -> 시간초과
N,M = map(int, input().split())
dud = []
all = []
for _ in range(N) :
    dud.append(input())
    
for _ in range(M) :
    bo = input()
    if bo in dud :
        all.append(bo)

all = sorted(all)

print(len(all))
for i in all :
    print(i)



# 딕셔너리로 풀기
N,M = map(int, input().split())
dct = {}
all = []
for _ in range(N) :
    dct[input()] = False
    
for _ in range(M) :
    bo = input()
    if bo in dct :
        all.append(bo)

all = sorted(all)

print(len(all))
for i in all :
    print(i)    


# set()
N,M = map(int, input().split())
a = set()
for _ in range(N) :
    a.add(input())

b = set()
for _ in range(M) :
    b.add(input())

all = sorted(list(a&b))

print(len(all))
for i in all :
    print(i)    
