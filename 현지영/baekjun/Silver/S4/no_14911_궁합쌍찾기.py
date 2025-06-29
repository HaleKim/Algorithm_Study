from itertools import combinations

nums = sorted(list(map(int, input().split())))
m = int(input())

ans = []
for comb in combinations(nums, 2) :
    if sum(comb) == m and comb not in ans:
        ans.append(comb)

for (a,b) in ans:
    print(f'{a} {b}')

print(len(ans))