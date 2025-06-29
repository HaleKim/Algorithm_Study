from itertools import permutations #순서가 다르면 다른 경우로 취급

n = int(input())  # n장의 카드
k = int(input())  # k개를 선택

cards = []
for _ in range(n):
    cards.append(input())  # string으로 list에 저장

lis = []
for group in permutations(cards, k) :
    ans = ''
    for g in group :
        ans += g
    if ans not in lis :
        lis.append(ans)

print(len(lis))