n = int(input())
for _ in range(n):
    cnt = 0
    k,m = map(int, input().split())
    s = [int(i) for i in input().split()]
    queue = [(i,j) for i, j in enumerate(s)]
    while queue:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            cnt+=1
            if cur[0] == m:
                print(cnt)
                break