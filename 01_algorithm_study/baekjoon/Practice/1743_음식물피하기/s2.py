import sys
sys.stdin = open("input.txt")

N, M, K = map(int, input().split())
trash = [[0] * M for _ in range(N)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
res = 0

for i in range(K):
    r, c = map(int, input().split())
    trash[r - 1][c - 1] = 1

def find_road(a, b):
    Q = [(a, b)]
    cnt = 0
    global res

    while Q:
        x, y = Q.pop(0)
        if cnt > res:
            res = cnt

        for l in range(4):
            nx = dx[l] + x
            ny = dy[l] + y

            if 0 <= nx < N and 0 <= ny < M:
                if trash[nx][ny] == 1:
                    trash[nx][ny] = 0
                    Q.append((nx, ny))
                    cnt += 1

for j in range(N):
    for k in range(M):
        if trash[j][k] == 1:
            find_road(j, k)

print(res)