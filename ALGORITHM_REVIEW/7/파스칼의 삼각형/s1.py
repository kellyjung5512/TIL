import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    pascal = [[0] * N for _ in range(N)] # 계산 후 정리할 공간
    print('#{}'.format(tc))
    pascal[0][0] = 1
    print(pascal[0][0])
    for i in range(1, N):
        for j in range(N):
            if j == 0:
                pascal[i][j] = 1
            else:
                pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]
            if pascal[i][j]:
                print(pascal[i][j], end=' ')
        print()

    # print(pascal)
