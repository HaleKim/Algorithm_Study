S = int(input())
ans, cnt = 0, 0 
for i in range(1,1000000000) :
    ans += i
    if ans > S :
        break
    cnt += 1
print(cnt)