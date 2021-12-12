import sys
sys.stdin = open('input.txt')

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    pool = [input() for _ in range(N)]
    visited = [[987654321] * M for _ in range(N)]

    Q = [0] * (N * M)
    front = -1
    rear = -1

    for i in range(N):
        for j in range(M):
            if pool[i][j] == 'W':
                rear += 1
                Q[rear] = (i, j)
                visited[i][j] = 0

    while front != rear:
        front += 1
        x, y = Q[front]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue

            if pool[nx][ny] == 'L' and visited[nx][ny] == 987654321:
                visited[nx][ny] = visited[x][y] + 1
                rear += 1
                Q[rear] = (nx, ny)

    ans = 0

    for i in visited:
        for j in i:
            ans += j

    print("#{} {}".format(tc, ans))