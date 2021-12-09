import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    A, B = map(str, input().split())
    i = 0
    cnt = 0
    while i < len(A):
        if A[i:i+len(B)] == B:
            cnt += 1
            i += len(B)
        else:
            i += 1
    text_length = len(A) - cnt * len(B) + cnt
    print('#{} {}'.format(tc, text_length))