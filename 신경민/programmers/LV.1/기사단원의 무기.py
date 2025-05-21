def solution(number, limit, power):
    cnt = [0] * (number + 1)
    
    for i in range(1, number + 1):
        for j in range(i, number + 1, i):
            cnt[j] += 1
    
    total = 0
    for i in cnt:
        if i > limit:
            total += power
        else:
            total += i
    
    return total

# 숫자만큼 리스트에 리스트를 만들고
# 1부터 숫자까지 차례대로 리스트에 문자열을 넣는다
# [[],[],[],[]] 4까지니까 1부터하면
# [[1],[1],[1],[1]] -> [[1],[1,2],[1],[1,2]] -> [[1],[1,2],[1,3],[1,2]] -> [[1],[1,2],[1,3],[1,2,4]]