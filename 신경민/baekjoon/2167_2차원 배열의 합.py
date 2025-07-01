N,M = map(int, input().split())
lis = []
answer=[]
lis = [[int(j) for j in input().split()] for _ in range(N)]

count = int(input())

for i in range(count):
    ans=0
    i,j,x,y = map(int, input().split())
    for j in range(j-1,y):
        for k in range(i-1, x):
            ans+=lis[k][j]
    answer.append(ans)

for i in answer:
    print(i)

# 시간초과
# pypy3는 통과~