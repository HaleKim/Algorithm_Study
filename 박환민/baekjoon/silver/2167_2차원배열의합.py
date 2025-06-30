# 시간복잡도를 줄이기 위해 누적합을 미리 구함 => 2중 for문으로 해결
# 미리 구해놓은 누적합 array를 돌면서(1중 for문) 결과값 return 가능

import sys
input = sys.stdin.readline

n , m = map(int, input().split())

array = [list(map(int, input().split())) for _ in range(n)]

k = int(input())

sum_array = [list(map(int, input().split())) for _ in range(k)]

cumsum = [[0]*(m+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,m+1):
        cumsum[i][j] = array[i-1][j-1] + cumsum[i-1][j] + cumsum[i][j-1] - cumsum[i-1][j-1]

for index in range(k):
    sum = 0
    i,j, x, y = sum_array[index]
    sum = cumsum[x][y] - cumsum[x][j-1] - cumsum[i-1][y] + cumsum[i-1][j-1]
    print(sum)