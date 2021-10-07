# indexerror : 간단한 실수 -> 가로의 길이 M, 세로의 길이 N이라고 해서 가로 세로가 아니라 행 열로 봐야함 바보야

import sys
sys.stdin = open('input.txt')

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(a, b):
    global result
    visited[a][b] = 1
    Q = [[a, b]]
    cnt = 1
    while Q:
        num = Q.pop(0)

        for i in range(4):
            nx = dx[i] + num[0]
            ny = dy[i] + num[1]

            if 0 <= nx < M and 0 <= ny < N and war[nx][ny] == war[num[0]][num[1]] and visited[nx][ny] == 0:
                    Q.append([nx, ny])
                    visited[nx][ny] = 1
                    cnt += 1
    return cnt


N, M = map(int, input().split())
war = [list(map(str, input())) for _ in range(M)]
visited = [[0 for _ in range(N)] for _ in range(M)]
W, B = 0, 0

for i in range(M):
    for j in range(N):
        if visited[i][j] == 0:
            result = bfs(i, j)
            if war[i][j] == 'W':
                W += result ** 2
            else:
                B += result ** 2

print(W, B)
