# 시작 시간 : 16:15
# 끝낸 시간 : (있을까?)
# 문제 사고 과정
# 1. N * N의 cell에 core 혹은 전선이 있음
# 2. 전선은 직선만, 교차 X
# 3. 어디에 전선이 붙든 전선의 개수가 최소화되면 될 듯 ? 그럼 BFS일 가능성이 있겠다.
import sys
sys.stdin = open('input.txt')

dx = [-1 , 1, 0, 0] # 상하좌우
dy = [0, 0, -1, 1]

def dfs(core_x, core_y):
    global cnt
    stack = [[core_x, core_y]]

    while stack:
        check = 0
        core = stack.pop(0)
        # print(core)
        for i in range(4):
            nx = core[0] + dx[i]
            ny = core[1] + dy[i]
            check += 1
            visited[nx][ny] = 1

            if i == 0:
                while 0 <= nx < N and 0 <= ny < N:
                    nx += dx[0]
                    ny += dy[0]
                    if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                        check += 1
                        visited[nx][ny] = 1
                    elif nx == 0 or nx == N-1 or ny == 0 or ny == N-1:
                        check = N * N
                        break

            elif i == 1:
                while 0 <= nx < N and 0 <= ny < N:
                    nx += dx[1]
                    ny += dy[1]
                    if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                        check += 1
                        visited[nx][ny] = 1
                    elif nx == 0 or nx == N-1 or ny == 0 or ny == N-1:
                        check = N * N
                        break


            elif i == 2:
                while 0 <= nx < N and 0 <= ny < N:
                    nx += dx[2]
                    ny += dy[2]
                    if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                        check += 1
                        visited[nx][ny] = 1
                    elif nx == 0 or nx == N - 1 or ny == 0 or ny == N - 1:
                        check = N * N
                        break

            elif i == 3:
                while 0 <= nx < N and 0 <= ny < N:
                    nx += dx[2]
                    ny += dy[2]
                    if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                        check += 1
                        visited[nx][ny] = 1
                    elif nx == 0 or nx == N - 1 or ny == 0 or ny == N - 1:
                        break
                        return check
            else:
                pass
    if cnt > check:
        cnt = check
    return cnt


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maxinos = [list(map(int, input().split())) for _ in range(N)]
    visited = maxinos[:]
    cnt = N * N
    for i in range(N):
        for j in range(N):
            if maxinos[i][j] == 1 and i != 0 and i != N-1 and j != 0 and j != N-1:
                core_x = i
                core_y = j
                # print(core_x)
                # print(core_y)
                dfs(core_x, core_y)
    print(cnt)

