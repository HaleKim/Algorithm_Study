N = int(input())
li = []
ans = 0
for _ in range(N) :
    li.append(int(input()))
li = sorted(li, reverse=True)

sam = []
for l in li :
    sam.append(l)
    if len(sam) == 3 :
        sam.remove(min(sam))
        for s in sam :
            ans += s
        sam = []
for s in sam :
    ans += s

print(ans)