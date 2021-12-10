import sys
sys.stdin = open('input.txt')

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y, distance):
    Q = [[x, y, distance]]

    while Q:
        row, col, cnt = map(int, Q.pop(0))
        visited[row][col] = 1

        if maze[row][col] == 3:
            return cnt-1

        for k in range(4):
            nx = row + dx[k]
            ny = col + dy[k]

            if 0 <= nx < N and 0 <= ny < N:
                if visited[nx][ny] == 0 and maze[nx][ny] != 1:
                    Q.append([nx, ny, cnt+1])

    return 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                ans = bfs(i, j, 0)
                break

    print('#{} {}'.format(tc, ans))
