import sys
sys.stdin = open('input.txt')

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]    # 우, 하, 좌, 상

find_tunnel = [
    [1, 3, 6, 7],
    [1, 2, 4, 7],
    [1, 3, 4, 5],
    [1, 2, 5, 6]
]

def find_road(num):
    if num == 1:
        delta = [0, 1, 2, 3]
    elif num == 2:
        delta = [1, 3]
    elif num == 3:
        delta = [0, 2]
    elif num == 4:
        delta = [0, 3]
    elif num == 5:
        delta = [0, 1]
    elif num == 6:
        delta = [1, 2]
    elif num == 7:
        delta = [2, 3]

    return delta


def bfs(x, y, cnt):
    Q = [(x, y, cnt)]

    while Q:
        r, c, cnt = Q.pop(0)

        if cnt > L:
            return

        visited[r][c] = cnt

        temp = find_road(maps[r][c])

        for i in range(len(temp)):
            nr = dx[temp[i]] + r
            nc = dy[temp[i]] + c
            if 0 <= nr < N and 0 <= nc < M:
                if maps[nr][nc] in find_tunnel[temp[i]]:
                    if visited[nr][nc] == 0:
                        Q.append((nr, nc, cnt + 1))

T = int(input())
for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    maps = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    res = 0

    bfs(R, C, 1)
    # print(visited)
    for i in range(len(visited)):
        for j in range(len(visited[i])):
            if visited[i][j] != 0:
                res += 1

    print('#{} {}'.format(tc, res))

# [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 5, 0, 0, 0, 0, 0],
#  [0, 0, 4, 3, 4, 5, 0, 0, 0, 0],
#  [0, 6, 5, 2, 3, 6, 7, 0, 0, 0],
#  [0, 0, 0, 1, 2, 5, 6, 0, 0, 0],
#  [0, 6, 5, 2, 3, 4, 5, 6, 0, 0],
#  [0, 5, 4, 3, 0, 0, 6, 7, 0, 0],
#  [7, 6, 5, 4, 0, 8, 7, 8, 0, 0],
#  [8, 7, 6, 5, 6, 7, 8, 0, 0, 0],
#  [9, 8, 0, 0, 7, 0, 0, 0, 0, 0]]

# def find_road(num):
#     if num == 1:
#         delta = [0, 1, 2, 3]
#     elif num == 2:
#         delta = [1, 3]
#     elif num == 3:
#         delta = [0, 2]
#     elif num == 4:
#         delta = [0, 3]
#     elif num == 5:
#         delta = [0, 1]
#     elif num == 6:
#         delta = [1, 2]
#     elif num == 7:
#         delta = [2, 3]
#
#     return delta
#
# def dfs(x, y, cnt):
#     visited[x][y] = cnt
#
#     if cnt == L:
#         return
#
#     temp = find_road(maps[x][y])
#
#     for i in range(len(temp)):
#         nr = dx[temp[i]] + x
#         nc = dy[temp[i]] + y
#         if nr < 0 or nr >= N or nc < 0 or nc >= M:
#             continue
#         if 0 <= nr < N and 0 <= nc < M and maps[nr][nc] != 0:
#             dfs(nr, nc, cnt + 1)
#
#
# T = int(input())
# for tc in range(1, T+1):
#     N, M, R, C, L = map(int, input().split())
#     maps = [list(map(int, input().split())) for _ in range(N)]
#     visited = [[0] * M for _ in range(N)]
#     res = 0
#
#     dfs(R, C, 1)
#
#     for i in range(N):
#         for j in range(M):
#             if visited[i][j] != 0:
#                 res += 1
#
#     print(res)