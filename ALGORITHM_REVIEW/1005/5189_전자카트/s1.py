import sys
sys.stdin = open('input.txt')

import itertools

dx = [0, 1]
dy = [1, 0]

def find_min(nums):
    location = 0
    cnt = 0
    ans = 0
    global result

    for i in nums:
        ans += electricity[location][i]
        location = i
        cnt += 1
        if cnt == N - 1:
            ans += electricity[location][0]
            if ans < result:
                result = ans

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    electricity = [list(map(int, input().split())) for _ in range(N)]

    num = [i for i in range(1, N)]
    num_list = list(itertools.permutations(num, len(num)))
    # print(num_list)
    result = 987654321
    for nums in num_list:
        find_min(nums)

    print('#{} {}'.format(tc, result))