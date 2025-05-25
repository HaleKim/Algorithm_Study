n = list(map(int, input('입력: ')))

answer = n[0]
for i in range(1, len(n)):
    if answer <= 1 or n[i] <= 1:
        answer += n[i]
    else:
        answer *= n[i]

print(answer)
