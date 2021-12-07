import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split()) # N만큼의 배열, M만큼의 파리채 배열
    arr = [list(map(int, input().split())) for _ in range(N)]
    check = []
    for i in range(N-M+1):
        for j in range(N-M+1):
            temp = 0
            for k in range(M):
                for l in range(M):
                    temp += arr[i+k][j+l]
            check.append(temp)
    print('#{} {}'.format(tc, max(check)))