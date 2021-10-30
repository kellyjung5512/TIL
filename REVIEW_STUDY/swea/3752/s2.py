import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cnt = 0
    nums = list(map(int, input().split()))
    result = set()
    for i in range(1 << N):  # 부분집합의 개수
        my_sum = []
        for j in range(N):
            if i & (1 << j):
                my_sum.append(nums[j])
        cnt = sum(my_sum)
        result.add(cnt)


    print('#{} {}'.format(tc, len(result)))