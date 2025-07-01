N, M = map(int, input().split())

dic = {}
for _ in range(N) :
    word = input()

    if len(list(word)) < M :
        continue

    if word in dic.keys() :
        dic[word] += 1
    else : #word not in dic.keys() :
        dic[word] = 1

dic = sorted(dic.items(), key = lambda x: (-x[1], -len(x[0]), x[0]))
for d in dic:
    print(d[0])
    