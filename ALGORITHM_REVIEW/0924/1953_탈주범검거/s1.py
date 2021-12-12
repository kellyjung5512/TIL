import sys
sys.stdin = open('input.txt')

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]    # 우, 하, 좌, 상

def find_road(num):
    if num == 1:
        delta = [0, 1, 2, 3]
    elif num == 2:
        delta = [1, 3]
    elif num == 3:
        delta = [0, 2]
    elif num == 4:
        delta = [0, 3]
    elif num == 5:
        delta = [0, 1]
    elif num == 6:
        delta = [1, 2]
    elif num == 7:
        delta = [2, 3]

    return delta

def dfs(x, y, cnt):
    visited[x][y] = 1
    if cnt == L : return

    temp = find_road(maps[x][y])

    for i in range(len(temp)):
        nr = dy[temp[i]] + x
        nc = dx[temp[i]] + y
        if nr < 0 or nr >= N or nc < 0 or nc >= M: continue
        if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == 0 and maps[nr][nc] != 0:
            dfs(nr, nc, cnt + 1)
            visited[x][y] = 0


T = int(input())
for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    maps = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(M)]
    res = []

    dfs(R, C, 0)

    print(dfs(R, C, 0))