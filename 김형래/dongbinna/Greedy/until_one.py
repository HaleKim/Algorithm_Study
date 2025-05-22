n, k = map(int, input("n, k : ").split())
cnt = 0

while(n > 1) :
    if n % k :
        n -= 1
        cnt += 1
    else :
        n //= k
        cnt += 1

print(cnt)