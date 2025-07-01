n = int(input())
lis = []
for _ in range(n):
    a = tuple(map(int, input().split()))
    lis.append(a)
lis = sorted(lis)
for i in lis:
    n, k = i
    print(n, k)