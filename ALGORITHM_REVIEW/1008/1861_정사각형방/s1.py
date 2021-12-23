import sys
sys.stdin = open('input.txt')

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(x, y, cnt):
    global result, room_number

    if cnt > result:
        room_number = room[x][y]
        result = cnt

    elif cnt == result:
        if room_number > room[x][y]:
            room_number = room[x][y]

    for k in range(4):
        nx = dx[k] + x
        ny = dy[k] + y

        if 0 <= nx < N and 0 <= ny < N and room[nx][ny] == room[x][y] - 1:
            dfs(nx, ny, cnt+1)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    room = [list(map(int, input().split())) for _ in range(N)]
    result = 1
    room_number = 1000000
    for i in range(N):
        for j in range(N):
            dfs(i, j, 1)    # 리스트의 좌표와 cnt 가지고 다니기
    print('#{} {} {}'.format(tc, room_number, result))