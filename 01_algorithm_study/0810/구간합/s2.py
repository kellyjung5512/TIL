import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    max_num = 0
    min_num = 1000000000
    for i in range(len(nums) - M + 1):
        tmp = sum(nums[i: i+M])
        if tmp > max_num:
            max_num = tmp
        if tmp < min_num:
            min_num = tmp

    print('#{} {}'.format(tc, max_num - min_num))