# 아주 쉽게 해결.. 단거리 구하기는 bfs로 풀어야지

import sys
sys.stdin = open("input.txt")

N, M = map(int, input().split())
miro = [list(map(int, input())) for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(a, b):
    Q = [(a, b)]
    if a == N - 1 and b == M - 1:
        return
    while Q:
        x, y = Q.pop(0)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                if miro[nx][ny] == 1:
                    miro[nx][ny] = miro[x][y] + 1
                    Q.append((nx, ny))

bfs(0, 0)
print(miro[N - 1][M - 1])