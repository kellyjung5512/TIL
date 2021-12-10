import sys
sys.stdin = open('input.txt')

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def find_road(x, y):
    # global ans
    # if maze[x][y] == 3:
    #     ans = 1
    #     return
    visited[x][y] = 1

    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y

        if 0 <= nx < 16 and 0 <= ny < 16:
            if maze[nx][ny] == 0 and visited[nx][ny] == 0:
                temp = find_road(nx, ny)
                if temp == 1:
                    return 1
                visited[nx][ny] = 0
            elif maze[nx][ny] == 3:
                return 1
    return 0

for tc in range(1, 11):
    T = int(input())
    maze = [list(map(int, input())) for _ in range(16)]
    visited = [[0] * 16 for _ in range(16)]
    # ans = 0
    ans = find_road(1, 1)
    print('#{} {}'.format(tc, ans))
