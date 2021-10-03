import sys
sys.setrecursionlimit(10000)
sys.stdin = open('input.txt')



def dfs(x, y):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if land[nx][ny] == 1:
                land[nx][ny] = 0
                dfs(nx, ny)

T = int(input())
for tc in range(1, T+1):
    M, N, K = map(int, input().split())
    land = [[0] * M for _ in range(N)]

    for i in range(K):
        x, y = map(int, input().split())
        land[y][x] = 1

    cnt = 0
    for j in range(N):
        for k in range(M):
            if land[j][k] == 1:
                dfs(j, k)
                cnt += 1
    print(cnt)
