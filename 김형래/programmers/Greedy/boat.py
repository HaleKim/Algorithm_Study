"""
성능 향상 필요
1. people이 커지면 순회하는데에 비용이 너무 크게 드므로 sorted 하고 순회를
처음부터가 아니라 끝에서부터 한다!
2. 매번 person+now <= limit하면 비용이 크게 드므로 limit - now 값을 미리 저장하고
그것과 비교한다!
3. sorted() 보다 arr.sort()가 성능상 낫다.


pop() 연산과 remove() 연산이 문제였다.
둘 다 연산을 수행한 뒤 요소들을 전부 한 칸씩 이동시켜줘야하기 때문에 시간복잡도가 커진다.
불필요한 리스트 수정은 지양!

나는 최대한 보트 limit에 맞춰서 사람들을 태우는 것이 최선이라고 생각하고
내림차순으로 정렬한 people에서 맨 앞부터 쭉 순회하며 거기서 조건을 만족하는 사람을 태웠는데,
(그렇게 한다면 내림차순으로 정렬돼있으므로 맨 앞(가장 무거운 사람)과 탈 수 있는 사람들 중
가장 무거운 사람을 태울 수 있으니까)
그렇게 할 필요 없이 그냥 가장 무거운 사람과 가장 가벼운 사람을 계속해서 짝지어가며
풀어도 되는 문제였다. 나도 처음에 이 생각 했는데 .......
"""
# def solution(people, limit):
#     answer = 0
#     sorted(people, reverse=True)
#     while people :
#         now = people.pop(0)
#         nlimit = limit - now
#         for person in people :
#             if person <= nlimit :
#                 people.remove(person)
#                 break
#         answer += 1
#     return answer

# def solution(people, limit):
#     answer, person, idx = 0,0,0
#     people.sort(reverse=True)
#     while people :
#         now = people.pop(0)
#         nlimit = limit - now
#         length = len(people)
#         for i in reversed(range(length)) :
#             person = people[i]
#             if person > nlimit :
#                 idx = i+1
#                 break
#         if idx < length :
#             people.pop(idx)
#             person,idx = 0,0
#         answer += 1
#     return answer

# def solution(people, limit):
#     answer, length = 0, len(people)
#     people.sort(reverse=True)
#     isboarded = [False]*length
    
#     for i in range(length) :
#         if isboarded[i] : # 이미 탄 사람인지 확인
#             continue
#         isboarded[i] = True # 안탔음 태운다
#         now = people[i]
#         nlimit = limit - now
#         answer += 1
        
#         for j in range(i+1, length) :
#             if people[j] <= nlimit and not isboarded[j]:
#                 isboarded[j] = True
#                 break
        
#     return answer

def solution(people, limit):
    people.sort()
    left, right = 0, len(people)-1
    answer = 0
    
    while left <= right:
        if people[left] + people[right] <= limit:
            left += 1
        right -= 1
        answer += 1
    
    return answer