import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    cost = list(map(int, input().split()))  # 1일, 1달, 3개월, 1년 요금
    plan = list(map(int, input().split()))  # 며칠 갈건지?
    idx = 0

    result = [0] * 14
    while idx < 14:
        money = 0                           # while문을 돌면서 가격 비교를 할 것임
        if idx < 12 and plan[idx] != 0:
            if plan[idx] * cost[0] >= cost[1]:
                result[idx] = cost[1]
            elif plan[idx] * cost[0] < cost[1]:
                result[idx] = plan[idx] * cost[0]
            idx += 1
        else:
            idx += 1

    # print(cost)
    # print(plan)
    print(sum(result))