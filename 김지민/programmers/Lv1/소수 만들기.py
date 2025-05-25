from itertools import combinations

def solution(nums): # 처음 풀이
    answer = 0

    combi = list(combinations(nums, 3))
    for c in combi:
        n = sum(c)
        for i in range(2, n):
            if n % i == 0:
                break
        if i == n-1:
            answer += 1
    
    return answer

from itertools import combinations

def solution2(nums): # 개선된 풀이
    # 소수 판별을 최적화하여 시간 복잡도를 줄임
    # n의 제곱근까지만 나누어 떨어지는지 확인
    # for-else 구문 사용
    answer = 0

    for c in combinations(nums, 3):
        n = sum(c)
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                break
        else:
            answer += 1
    
    return answer