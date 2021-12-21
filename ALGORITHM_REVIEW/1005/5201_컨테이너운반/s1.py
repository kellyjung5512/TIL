import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    weight = list(map(int, input().split()))
    tons = list(map(int, input().split()))
    weight.sort(key=lambda x: -x)
    tons.sort(key=lambda x: -x)
    # print(weight)
    # print(tons)

    result = 0
    for i in range(len(tons)):
        for j in range(len(weight)):
            if weight[j] != 0:
                if tons[i] >= weight[j]:
                    tons[i] -= weight[j]
                    result += weight[j]
                    weight[j] = 0
                    break
            if tons[i] == 0:
                continue
    print('#{} {}'.format(tc, result))