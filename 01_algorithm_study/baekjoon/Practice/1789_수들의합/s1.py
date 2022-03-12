import sys
sys.stdin = open('input.txt')

# 흠 완전 수학 문제였군
num = int(input())
n = 1
while n * (n+1) / 2 <= num:
    n += 1
print(n - 1)