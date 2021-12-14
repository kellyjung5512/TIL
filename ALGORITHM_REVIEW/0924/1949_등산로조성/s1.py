import sys
sys.stdin = open('input.txt')

T = int(input())

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1] # 하

def dfs(x, y, cnt, one_time):
    global ans

    if cnt > ans:
        ans = cnt

    visited[x][y] = 1

    for k in range(4):
        nr = dx[k] + x
        nc = dy[k] + y

        if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0:
            if mountain[nr][nc] < mountain[x][y]:
                dfs(nr, nc, cnt + 1, one_time)

            elif one_time:
                for l in range(1, K + 1):
                    mountain[nr][nc] -= l
                    one_time = 0
                    if mountain[nr][nc] < mountain[x][y]:
                        dfs(nr, nc, cnt + 1, one_time)
                    mountain[nr][nc] += l
                    one_time = 1

    visited[x][y] = 0
    # return ans

for tc in range(1, T+1):
    N, K = map(int, input().split())
    mountain = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    # print(mountain)
    max_height = 0
    for i in range(N):
        for j in range(N):
            if mountain[i][j] > max_height:
                max_height = mountain[i][j]
    # print(max_height)
    ans = 0
    for i in range(N):
        temp = 1
        for j in range(N):
            if mountain[i][j] == max_height:
                dfs(i, j, temp, 1)

    print('#{} {}'.format(tc, ans))