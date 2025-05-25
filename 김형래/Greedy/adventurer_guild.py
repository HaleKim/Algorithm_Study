# n = int(input())
# fear = sorted(map(int, input().split()), reverse=True)
# i, cnt = 0, 0

# while i < n :
#   match fear[i] :
#     case 3 :
#       if i + 2 > n :
#         break
#       i += 3
#       cnt += 1
#     case 2 :
#       if i + 1 > n :
#         break
#       i += 2
#       cnt += 1
#     case 1 :
#       i += 1
#       cnt += 1
# print(cnt)
# 잘못 생각해서 높은놈부터 해버림..

n = int(input())
fear = sorted(map(int, input().split()))
cnt, ans = 0, 0

for i in fear :
  cnt += 1
  if i == cnt : # cnt >= i 로 설정해야함
    ans += 1
    cnt = 0

print(ans)