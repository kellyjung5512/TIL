import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    check = []
    for i in range(len(nums)-M+1):
        result = 0
        for j in range(M):
            result += nums[i+j]
        check.append(result)
    print('#{} {}'.format(tc, max(check)-min(check)))