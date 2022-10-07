import sys
sys.stdin = open('input.txt')

A, B = map(int, input().split())
a, b = A, B

# 유클리드 호제법
while b != 0:
    a = a % b
    a, b = b, a

# gcd
print(a)

# lcm
print(A * B // a)