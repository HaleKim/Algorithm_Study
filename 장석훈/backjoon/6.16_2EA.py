##ㅡㅡㅡㅡㅡㅡ1620 ..블로그참고하였음음

# n포켓몬, m문제개수 ->양방향매핑 (이름->번호,번호->이름)
import sys

input = sys.stdin.readline
N, M = map(int, input().split())

# 이름 → 번호 dict
name_to_num = {}
# 번호 → 이름 list
num_to_name = [''] * (N + 1)

# 포켓몬 입력
for i in range(1, N + 1):
    name = input().strip()  
    name_to_num[name] = i   # 이름 → 번호 매핑
    num_to_name[i] = name   # 번호 → 이름 저장

# 문제 처리
for _ in range(M):
    query = input().strip()
    
    # 숫자인 경우 → 번호 → 이름 출력
    if query.isdigit():
        print(num_to_name[int(query)])
    else:
        # 이름인 경우 → 이름 → 번호 출력
        print(name_to_num[query])


##ㅡㅡㅡㅡㅡㅡㅡㅡ1110

