N, K = map(int, input().split())

A = [i for i in range(2,N+1)]
cnt = 0
for _ in range(N) :
    num = A[0]
    A.remove(num)
    i = 1
    cnt += 1
    if cnt == K :
        break
    while num < A[-1] :
        i+=1
        if num*i in A :
            A.remove(num*i)
            cnt += 1
            if cnt == K :
                break
print(num)
