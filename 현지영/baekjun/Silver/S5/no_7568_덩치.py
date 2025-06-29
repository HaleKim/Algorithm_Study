N = int(input())  # 전체 사람의 수
people = []
for _ in range(N) :
    people.append(tuple(map(int, input().split())))

for p in people :
    rank = 1
    for p2 in people :
        if p[0] < p2[0] and p[1] < p2[1] :
            rank += 1
    print(rank, end=' ')

