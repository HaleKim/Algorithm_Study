
n = int(input())
original = n

cnt = 0 

while True:
    cnt += 1

    if n < 10 :
        n_list = [0,n]
    else : 
        n_list = list(str(n))

    sum_position = 0
    for i in n_list :
        sum_position += int(i)

    n = int(str(n)[-1] + str(sum_position)[-1])

    if original == n :
        break

print(cnt)

