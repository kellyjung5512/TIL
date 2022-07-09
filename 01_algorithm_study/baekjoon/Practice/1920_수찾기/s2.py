# 이분탐색으로 해결 -> google에 검색했음 ㅠ..ㅠ
# 다시 한 번 해보기

import sys
sys.stdin = open('input.txt')

N = int(input())
A = sorted(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

def binary(j, A_list, start, end):
    if start > end:
        return 0
    tmp = (start + end) // 2
    if j == A_list[tmp]:
        return 1
    elif j < A_list[tmp]:
        return binary(j, A_list, start, tmp-1)
    else:
        return binary(j, A_list, tmp+1, end)

for i in B:
    start = 0
    end = len(A)-1
    print(binary(i, A, start, end))
