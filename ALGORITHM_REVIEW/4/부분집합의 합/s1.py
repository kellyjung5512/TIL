import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    A = [i for i in range(1, 13)]
    # print(A)
    # check = []
    cnt = 0
    for i in range(1 << len(A)):
        lst = []
        for j in range(len(A)):
            if i & (1 << j):
                lst.append(A[j])
            if len(lst) > N:
                break
        if len(lst) == N and sum(lst) == K:
            cnt += 1
    print('#{} {}'.format(tc, cnt))