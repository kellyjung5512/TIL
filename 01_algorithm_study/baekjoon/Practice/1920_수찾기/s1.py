# 굉장히 단순하게 풀었더니 시간 초과
# 범위가 넓을 때 단순하게 풀면 안되나? ex) 2^32

import sys
sys.stdin = open('input.txt')

N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

for num in B:
    if num in A:
        print(1)
    else:
        print(0)