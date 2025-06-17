#프로그래머스 4문제

# 소수찾기(63%)
def solution(n):
    answer = 0
    lis = [0] * n  # 크기가 n인 리스트 생성 후 해당 숫자의 약수를 저장함함
    
    # 약수 개수 구하기
    for i in range(1, n + 1):  # 1부터 n까지 
        for j in range(i, n + 1, i):  # i의 배수인 j
            lis[j - 1] += 1  # j의 약수+= 1
    
    for i in lis:
        if i == 2:  # 약수의 개수가 정확히 2개 → 소수임 (1과 자신)
            answer += 1
    
    return answer

#두뽑 더하기(73%)
def solution(numbers):
    result = set()  # 중복제거

    # 두 수를 고르는 조합구하기기
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):  # i와 겹치지 않게
            result.add(numbers[i] + numbers[j])  # 두 수의 합을 set에 추가

    return sorted(result)# set을 리스트화&정렬

# k번째 수(72%)

#array와 i j k 리스트 ->array[i-1:j] 잘라서 정렬후 k번째를 결과리스트에 추가
def solution(array, commands):
    result = []
    
    for ijk in commands:
        i, j, k = ijk  # i, j, k 풀어서 받기
        sliced = array[i-1:j]  # i번째부터 j번째까지 슬라이싱
        sliced.sort()  # 정렬
        result.append(sliced[k-1])  # k번째 값 추가 
    
    return result

#약수 개수와 덧셈(84%)

# left->right 범위에서 약수갯수가 짝수면 더하고, 홀수면 뺀 누적합 구하기
def solution(left, right):
    answer = 0
    
    for num in range(left, right + 1):
        # 제곱수인지 확인
        if int(num ** 0.5) == num ** 0.5:
            answer -= num  
        else:
            answer += num  
    
    return answer