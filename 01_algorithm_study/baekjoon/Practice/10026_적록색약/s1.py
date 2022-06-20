from collections import deque
import sys
sys.stdin = open('input.txt')
# input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    q.append([x, y])
    check[x][y] = cnt
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if grape[nx][ny] == grape[x][y] and check[nx][ny] == 0:
                    q.append([nx, ny])
                    check[nx][ny] = 1

N = int(input())

grape = [list(map(str, input())) for _ in range(N)]
check = [[0] * N for _ in range(N)]

q = deque()
cnt = 0
result = [0, 0]

for i in range(N):
    for j in range(N):
        if check[i][j] == 0:
            bfs(i, j)
            cnt += 1
result[0] = cnt
cnt = 0

for i in range(N):
    for j in range(N):
        if grape[i][j] == 'R':
            grape[i][j] = 'G'
check = [[0]*N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if check[i][j] == 0:
            bfs(i, j)
            cnt += 1
result[1] = cnt

print(*result)