import sys
sys.stdin = open('input.txt')

dx = [0, 1]
dy = [1, 0]

def dfs(x, y, ans):
    global result
    ans += puzzle[x][y]

    if x == N-1 and y == N-1:
        if ans < result:
            result = ans

    visited[x][y] = 1

    for i in range(2):
        nx = dx[i] + x
        ny = dy[i] + y

        if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
            if ans > result:
                break
            dfs(nx, ny, ans)
            visited[nx][ny] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    puzzle = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    result = 987654321
    dfs(0, 0, 0)

    print('#{} {}'.format(tc, result))