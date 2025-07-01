n,m = map(int, input().split())
dogam = {}
answer=[]
for i in range(n):
    inp = input()
    dogam[i+1] = inp
    dogam[inp]= i+1
for _ in range(m):
    ans = input()
    if ans.isdigit():
        answer.append(dogam[int(ans)])
    else:
        answer.append(dogam[ans])
for i in answer:
    print(i) 