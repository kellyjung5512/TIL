import sys
sys.stdin = open("input.txt")
sys.setrecursionlimit(10000)

T = int(input())
for tc in range(T):
    M, N, K = map(int, input().split())
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    land = [[0] * N for _ in range(M)]
    for _ in range(K):
        X, Y = map(int, input().split())
        land[X][Y] = 1

    def dfs(a, b):
        land[a][b] = 0
        for k in range(4):
            nx = a + dx[k]
            ny = b + dy[k]

            if 0 <= nx < M and 0 <= ny < N:
                if land[nx][ny] == 1:
                    dfs(nx, ny)

    cnt = 0
    for i in range(N):
        for j in range(M):
            if land[j][i] == 1:
                dfs(j, i)
                cnt += 1

    print(cnt)
