N, K = map(int, input().split())

a = [0]*(N+1)
for i in range(1, N+1):
    for j in range(i, N+1, i):
        a[j] += 1

so_lis = []
for i in range(2, N+1):
    if a[i] == 2:
        so_lis.append(i)

n_lis = [i for i in range(2, N+1)]
cnt = 0

for i in so_lis:
    for j in range(i, N+1, i):
        if j in n_lis:
            n_lis.remove(j)
            cnt += 1
            if cnt == K:
                print(j)
                break
    if cnt == K:
        break