N,M = map(int, input().split())
word_lis=[]
for _ in range(N):
    alpha = input()
    if len(alpha) >= M:
        word_lis.append(alpha)
word_dict = {}

for i in set(word_lis):
    word_dict[i] = word_lis.count(i)

for i in sorted(word_dict)[::-1]:
    print(i)

# 시간초과
# 틀림 포기 ㅈㅈ
# 정렬이 너무 안됨