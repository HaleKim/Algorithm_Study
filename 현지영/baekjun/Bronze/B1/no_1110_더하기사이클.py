N = list(input())
if len(N)==1 :
    N = ['0']+N
a, b = int(N[0]), int(N[1])
num = a*10 + b
i = 0
while True :
    i+=1
    new = (a+b)%10 + b*10
    if new == num :
        break
    a = new // 10
    b = new % 10

print(i)