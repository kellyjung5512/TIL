import sys
sys.stdin = open("input.txt")
N, M = map(int, input().split())
w_power = 0
b_power = 0
maps = [list(input()) for _ in range(M)]
visited = [[0] * N for _ in range(M)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def dfs(x, y, cnt):
    visited[x][y] = 1
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < N and 0 <= ny < M:
            if visited[nx][ny] == 0 and maps[x][y] == maps[nx][ny]:
                cnt = dfs(nx, ny, cnt + 1)
    return cnt
for i in range(N):
    for j in range(M):
        if visited[i][j] == 0:
            if maps[i][j] == "W":
                w_power += dfs(i, j, 1) ** 2
            else:
                b_power += dfs(i, j, 1) ** 2
print(w_power, b_power)
