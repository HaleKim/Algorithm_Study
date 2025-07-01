n = int(input())
num=0
ans=1
while True:
    num+=ans
    if num > n:
        print(ans-1)
        break
    elif num==n:
        print(ans)
        break
    ans+=1