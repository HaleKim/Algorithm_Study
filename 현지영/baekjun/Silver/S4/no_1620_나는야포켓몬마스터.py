n, m = map(int, input().split())
name_dic = {}
num_dic = {}
ans = []
for i in range(n) :
    name = input()
    name_dic[f'{i+1}'] = name
    num_dic[name] = f'{i+1}'
for i in range(m) :
    q = input()
    if q in num_dic.keys() :
        ans.append(num_dic[q])
    else:
        ans.append(name_dic[q])

for a in ans :
    print(a)
# 시간 5304ms는 너무 긴거 아닌가...?

n, m = map(int, input().split())
n_dic = {}
n_list = [0]
ans = []
for i in range(1,n+1) :
    name = input()
    n_list.append(name)
    n_dic[name] = i

for i in range(m) :
    q = input().rstrip()
    if q.isdigit() :
        ans.append(n_list[int(q)])
    elif q.isalpha() :
        ans.append(n_dic[q])

for a in ans :
    print(a)
