# 이분탐색 안쓰고 set으로 받으면 해결 완료

import sys
sys.stdin = open('input.txt')

N = int(input())
A = set(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

for num in B:
    if num in A:
        print(1)
    else:
        print(0)