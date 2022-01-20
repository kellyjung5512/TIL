import sys
sys.stdin = open('input.txt')

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    Q = [(x, y)]

    while Q:
        step = Q.pop(0)

        for i in range(4):
            nx = dx[i] + step[0]
            ny = dy[i] + step[1]

            if 0 <= nx < N and 0 <= ny < M and miro[nx][ny] == 1:
                miro[nx][ny] = miro[step[0]][step[1]] + 1
                Q.append([nx, ny])

N, M = map(int, input().split())
miro = [list(map(int, input())) for _ in range(N)]
bfs(0, 0)
print(miro[N-1][M-1])