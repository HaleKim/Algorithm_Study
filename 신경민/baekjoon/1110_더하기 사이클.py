n = int(input())
cnt=0
ans = n
while True:
    if ans < 10:
        ans= int(str(ans)+str(ans))
        cnt+=1
    else:
        ans = int(str(ans)[1]+str(int(str(ans)[0])+int(str(ans)[1]))[-1])
        cnt+=1
    if ans == n:
        break
print(cnt)