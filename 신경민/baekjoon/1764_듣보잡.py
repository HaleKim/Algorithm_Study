# 나
n,m = map(int, input().split())
res=[input() for _ in range(n+m)]

ans = [i for i in list(set(res)) if res.count(i) == 2]

print(len(ans))
for i in ans:
    print(i)


#블로그
n,m = map(int, input().split())
set1 = set()
set2 = set()

for _ in range(n):
    set1.add(input())

for _ in range(m):
    set2.add(input())

result = sorted(list(set1 & set2))

print(len(result))

# 듣보잡 이름
for x in result:
    print(x)