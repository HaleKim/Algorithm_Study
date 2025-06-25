###프로그래머스 3문제

## 예산(77%)

# 소액우선, 누적합을 유지하면서 예산초과시점까지만 부서count
# 초과 시 그 이전까지 누적수가 result
def solution(d,budget):
    d.sort()
    total=0 #현 사용한 예산
    result=0
    for money in d:
        total+=money
        if total<=budget:
            result+=1
        else:
            break    
    return result

## 폰켓몬(67%)

#몬 len(nums) 마리 중 선택은 절반
# 번호가 같으면 하나, 최대한 다양한종류
# set() : 중복없는 고유한 값 자료집합
# set([3,1,2,3])={1,2,3}
## 가장많은종류= 절반만큼 챙기던가 종류가 한정적이라면 그 종류만큼
def solution(nums):
    max_=len(nums)//2
    type_=set(nums) 
    return min(len(type_),max_)

## 과일장수(64%)

# 고점부터 포장, 상자속 최저점*min으로 가격결정
# 정렬 후 박스집합을 생성, box가 m개보다 적으면 break
def solution(k, m, score):
    score.sort(reverse=True) #고점부터시작
    result=0
    for i in range(0,len(score),m):
        box=score[i:i+m]
        if len(box)<m:
            continue
        result+=min(box)*m
    #이익이 발생하지 않는 경우가 있나?
    return result

# 문자열 내마음대로 정렬하기
#ord('a') -> 97....


def solution(strings, n):
    idx=[]
    for i in range(len(strings)):
        idx.append((strings[i][n],strings[i]))
    idx.sort()
    # ('u','sun')...튜플로 만듬
    #튜플로 sort를 돌리면 첫번째 값 기준으로 정렬된다.
    #하지만 첫번째가 같다면? 두번째부터 정렬
    answer = [item[1] for item in idx]
    return answer