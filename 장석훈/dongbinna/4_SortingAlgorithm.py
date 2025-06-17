'''정렬알고리즘 비교 *수행시간과 데이터타입
선택 - 가장 작은데이터를 맨앞과 바꿈(반복)
삽입 - 첫번째 데이터를 두고, 두번째부터 판단하여 적절한 위치에 삽입
퀵 - 기준을 설정하고 큰것과 작은것의 위치를 바꿈 *일반적 가장많이사용
계수 -(조건:정수형태) 각 데이터 인덱스의 값을 증가시키며 정렬->중복등장에 효과적적

'''

## 문제. 두 배열의 원소 교체
#최대 k번 바꿔치기연산을 수행하여 만든 배열A 모든원소의 합의 최댓값 출력

# *매 시행마다 A의 최소값을 B의 최댓값과 교체하기
n,k=map(int,input().split())
a=list(map(int,input().split())) 
b=list(map(int,input().split()))

a.sort() #오름차순
b.sort(reverse=True) #내림차순

for i in range(k): # k번 비교
    if a[i]<b[i]:
        a[i],b[i]=b[i],a[i] # A가 B보다 작은 두 원소 교체
    else: 
        break
print(sum(a))