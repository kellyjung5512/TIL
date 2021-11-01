import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))
    result = set()
    for i in range(1 << N):
        temp = 0
        for j in range(N):
            if i & (1 << j):
                temp += nums[j]
        result.add(temp)
    print('#{} {}'.format(tc, len(result)))