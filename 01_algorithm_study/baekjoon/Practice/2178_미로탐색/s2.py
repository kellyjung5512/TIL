# dfs로 풀었다가 망한 상태 ㅋㅋ..~
# 다시 풀어보자

import sys
sys.stdin = open("input.txt")

N, M = map(int, input().split())
miro = [list(map(int, input())) for _ in range(N)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
visited = [[0] * M for _ in range(N)]

def find_road(x, y):
    visited[x][y] = 1
    if x == N - 1 and y == M - 1:
        return miro[x][y]
    else:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                if miro[nx][ny] == 1 and visited[nx][ny] == 0:
                    miro[nx][ny] = miro[x][y] + 1
                    find_road(nx, ny)
    return miro[N - 1][M - 1]

print(find_road(0, 0))
print(miro[N - 1][M - 1])