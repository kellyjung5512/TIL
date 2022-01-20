import sys
sys.stdin = open('input.txt')

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]   # 상 좌 하 우

def can_go(start_x, start_y):
    stack = [(start_x, start_y)]

    while stack:
        temp = stack.pop()
        x, y = temp[0], temp[1]

        maze[x][y] = 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N and maze[nx][ny] != 1:
                if maze[nx][ny] == 3:
                    return 1
                stack.append((nx, ny))

    return 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                m = i
                n = j
                break

    ans = can_go(m, n)
    print('#{} {}'.format(tc, ans))