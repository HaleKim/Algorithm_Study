n = int(input())
answer=0
while True:
    if n % 5 == 0:
        answer+=n//5
        break
    else:
        n -= 3
        answer+=1
    if n < 0:
        answer=-1
        break
print(answer)