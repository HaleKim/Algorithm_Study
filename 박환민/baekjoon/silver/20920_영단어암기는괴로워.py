import sys
input = sys.stdin.readline 

n, m = map(int, input().split())

word = [input().rstrip() for _ in range(n)]

cnt = {}

for i in word:
    if i in cnt :
        cnt[i] += 1
    else :
        cnt[i] = 1

# 딕셔너리 정렬은 sorted
cnt_sorted = sorted(cnt.items(), reverse = True)

# sort의 key파라미터
# 우선순위에 맞게 key를 지정해주면 됨
cnt_sorted.sort(key = lambda x: (-x[1], -len(x[0]), x[0])) # cnt는 1열 => -x[1]로 내림차순 정렬
# 정렬 기준 값이 같은 경우, 길이가 긴 순으로 내림차순 정렬

answer = []
for i, _ in cnt_sorted:
    if len(i) >= m :
        answer.append(i)

sys.stdout.write('\n'.join(answer))