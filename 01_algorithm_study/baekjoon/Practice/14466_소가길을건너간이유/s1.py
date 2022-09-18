import sys
from collections import deque
sys.stdin = open("input.txt")

N, K, R = map(int, input().split())
dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]

road = [[[] for _ in range(N + 1)] for _ in range(N + 1)]
cow_map = [[False for _ in range(N + 1)] for _ in range(N + 1)]
cow_list = []
cnt = 0

for _ in range(R):
    r1, c1, r2, c2 = map(int, input().split())
    road[r1][c1].append([r2, c2])
    road[r2][c2].append([r1, c1])

for _ in range(K):
    y, x = map(int, input().split())
    cow_list.append([y, x])
    cow_map[y][x] = True

def find_cow(y, x):
    global K, cnt
    visited = [[False for _ in range(N + 1)] for _ in range(N + 1)]
    q = deque()
    q.append([y, x])
    cow_map[y][x] = False
    tmp = 0
    K -= 1
    while q:
        cy, cx = q.popleft()
        for d in range(4):
            ny, nx = cy + dy[d], cx + dx[d]
            if 1 <= ny <= N and 1 <= nx <= N and not visited[ny][nx]:
                if [ny, nx] not in road[cy][cx]:
                    q.append([ny, nx])
                    visited[ny][nx] = True
                    if cow_map[ny][nx]:
                        tmp += 1
    cnt += K - tmp

for y, x in cow_list:
    if cow_map[y][x]:
        find_cow(y, x)

print(cnt)