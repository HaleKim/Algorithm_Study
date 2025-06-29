n = int(input())
lines = []
result = []
for _ in range(n) :
    lines.append(list(input()))
for line in lines :
    cnt = 0
    if line.count('(') != line.count(')') :
        ans = 'NO'
        result.append(ans)
        continue
    for l in line :
        if l == '(' :
            cnt += 1
        elif l == ')' :
            cnt -= 1
        if cnt < 0 :
            ans = 'NO'
            break
        ans = 'YES'
    result.append(ans)
for r in result :
    print(r)