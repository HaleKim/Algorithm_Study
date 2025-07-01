A, B = map(int, input().split())
total = A*B
if A % B == 0 :
    print(B)
    print(A)
else :
    C = 1
    while C != 0 :
        C = A % B
        A = B
        B = C

    print(A)
    print(int(total/A))