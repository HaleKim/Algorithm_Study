N, M, K = map(int, input().split()) #N명, M개 장르, 본선K명

dic = {}
for i in range(1,N+1) :
    dic[i]=0.0

for _ in range(M) :
    lis = list(input().split())
    for j in range(int(len(lis)/2)) : # 0부터 len(lis)/2까지
        if dic[int(lis[2*j])] < float(lis[2*j+1]) :
            dic[int(lis[2*j])] = float(lis[2*j+1])

dic = sorted(dic.items(), key=lambda x: -x[1])

cnt, ans = 0, 0
for k,v in dic :
    ans += v 
    cnt += 1
    if cnt == K :
        break

print(round(ans, 1))