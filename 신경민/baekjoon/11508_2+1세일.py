N = int(input())
u_lis = sorted([int(input()) for _ in range(N)])[::-1]

two_lis = [u_lis[i:i+3] for i in range(0, N, 3)]

ans=0
for i in two_lis:
    if len(i) == 3:
        ans+=(i[0]+i[1])
    else:
        ans+=sum(i)
print(ans)