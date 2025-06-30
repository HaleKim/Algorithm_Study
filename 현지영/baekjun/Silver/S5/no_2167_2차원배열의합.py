N, M = map(int, input().split())
nums = {}
for i in range(N) :
    nums[i] = input().split()

K = int(input())
answer = []
for _ in range(K):
    ans = 0
    i, j, x, y = map(int, input().split())
    for n in range(i-1,x) :
        for m in range(j-1,y) :
            ans += int(nums[n][m])
    answer.append(ans)

for a in answer :
    print(a)