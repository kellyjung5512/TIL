import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(2500)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < M:
            if baechu[nx][ny] == 1:
                baechu[nx][ny] = 0
                dfs(nx, ny)

T = int(input())
for tc in range(1, T+1):
    M, N, K = map(int, input().split())
    baechu = [[0 for _ in range(M)] for _  in range(N)]

    for i in range(K):
        x, y = map(int, input().split())
        baechu[y][x] = 1

    cnt = 0
    for j in range(N):
        for k in range(M):
            if baechu[j][k] == 1:
                dfs(j, k)
                cnt += 1
    print(cnt)