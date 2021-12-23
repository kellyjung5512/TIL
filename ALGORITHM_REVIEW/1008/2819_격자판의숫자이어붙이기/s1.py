import sys
sys.stdin = open('input.txt')

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, my_str):
    global result
    if len(my_str) == 7:
        result.add(my_str)
        return

    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y

        if 0 <= nx < 4 and 0 <= ny < 4:
            dfs(nx, ny, my_str + grid[nx][ny])



T = int(input())
for tc in range(1, T+1):
    grid = [list(input().split()) for _ in range(4)]
    result = set()

    for i in range(4):
        for j in range(4):
            dfs(i, j, grid[i][j])

    result = len(set(result))
    print('#{} {}'.format(tc, result))