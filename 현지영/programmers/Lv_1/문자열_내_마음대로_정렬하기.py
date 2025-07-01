# def solution(strings, n):
#     strings = sorted(strings) # 사전순으로 바꾸기 (같은 경우 방지)
#     check = []
#     for i,word in enumerate(strings) :
#         check.append((word[n],i))  # 인덱스의 알파벳과 실제 글자 순
#     check=sorted(check)
#     ans = []
#     for c,num in check :
#         ans.append(strings[num])
#     return ans

def solution(strings, n):
    strings=sorted(strings)
    return sorted(strings, key=lambda x: x[n]) 
