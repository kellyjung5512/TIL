import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    ingredient = list(map(int, input().split()))
    K = int(input())
    medicine = [list(map(int, input().split())) for _ in range(N)]
    effect = [[0]*N for _ in range(N)]
    max_effect = 0

    for i in range(N):
        for j in range(i, N):
            effect[i][j] = medicine[i][j] + medicine[j][i]


    while K >= 0:
        for i in range(N):
            for j in range(i, N):
                if max_effect < effect[i][j] and ingredient[i] != 0 and ingredient[j] != 0:
                    max_effect = effect[i][j]
                    r, c = i, j

        temp = min(ingredient[r], ingredient[c])
        if K <= temp:
            ans = max_effect
            print('#{} {}'.format(tc, ans))
            break

        else:
            K -= temp
            ingredient[r] -= temp
            ingredient[c] -= temp

            for i in range(N):
                for j in range(i, N):
                    if max_effect == effect[i][j]:
                        effect[i][j] = 0

            max_effect = 0