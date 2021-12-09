import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cost = list(map(int, input().split()))
    profit = []
    x = N - 1
    max_cost = cost[-1]
    ans = 0
    while x >= 0:
        if cost[x] > max_cost:
            while profit:
                temp = profit.pop()
                ans += max_cost - temp
            max_cost = cost[x]
            x -= 1
        else:
            profit.append(cost[x])
            x -= 1
    while profit:
        temp = profit.pop()
        ans += max_cost - temp
    print('#{} {}'.format(tc, ans))