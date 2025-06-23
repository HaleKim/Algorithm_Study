import math

num1, num2 = map(int, input().split())

gcd = math.gcd(num1,num2)
lcm = (num1 * num2) // gcd

print(gcd)
print(lcm)
