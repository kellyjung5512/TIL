import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    check = [[0]*N for _ in range(N)]
    x, y = 0, -1
    k = 0
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    cnt = 1
    while cnt <= N*N:
        nx, ny = x+dx[k], y+dy[k]
        if 0 <= nx < N and 0 <= ny < N and check[nx][ny] == 0:
            check[nx][ny] = cnt
            x, y = nx, ny
            cnt += 1
        else:
            k = (k+1) % 4
    print('#{}'.format(tc))
    for i in range(len(check)):
        print(*check[i])
