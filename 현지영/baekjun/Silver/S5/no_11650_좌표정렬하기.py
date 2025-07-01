N = int(input())
lis = []
for _ in range(N):
    (a,b) = map(int, input().split())
    lis.append((a,b))

for num1, num2 in sorted(lis) :
    print(f'{num1} {num2}')
