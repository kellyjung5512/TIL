import sys
sys.stdin = open("input.txt")

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

def dfs(x, y, cnt):
    if visited[x][y] == 0:
        visited[x][y] = 1
        for a in range(4):
            nx = x + dx[a]
            ny = y + dy[a]
            if 0 <= nx < N and 0 <= ny < M:
                if person[x][y] == person[nx][ny] and visited[nx][ny] == 0:
                    cnt = dfs(nx, ny, cnt + 1)
        return cnt


N, M = map(int, input().split()) # N이 가로, M이 세로
person = [list(map(str, input())) for _ in range(M)]
visited = [[0] * N for _ in range(M)]
white = 0
blue = 0

for i in range(N):
    for j in range(M):
        if visited[i][j] == 0:
            if person[i][j] == "W":
                white += dfs(i, j, 1) ** 2
            else:
                blue += dfs(i, j, 1) ** 2

print(white, end=" ")
print(blue, end=" ")