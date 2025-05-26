import math

def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a%b)
    
print(gcd(192, 162)) # 재귀 사용용
print(math.gcd(192, 162)) # math.gcd() 사용