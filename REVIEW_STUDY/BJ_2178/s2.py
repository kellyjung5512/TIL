import sys
sys.stdin = open('input.txt')

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(a, b):
    Q = [[a, b]]
    while Q:
        point = Q.pop(0)
        x, y = point[0], point[1]

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0 <= nx < N and 0 <= ny < M and miro[nx][ny] == 1:
                Q.append([nx, ny])
                miro[nx][ny] = miro[x][y] + 1



N, M = map(int, input().split())
miro = [list(map(int, input())) for _ in range(N)]
bfs(0, 0)
print(miro[N-1][M-1])