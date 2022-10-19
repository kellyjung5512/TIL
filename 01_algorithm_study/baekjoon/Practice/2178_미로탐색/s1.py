import sys
from collections import deque
sys.stdin = open("input.txt")

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    queue = deque()
    queue.append([x, y])
    while queue:
        temp = queue.popleft()
        for i in range(4):
            nx = temp[0] + dx[i]
            ny = temp[1] + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if roadmap[nx][ny] == 1:
                    roadmap[nx][ny] = roadmap[temp[0]][temp[1]] + 1
                    queue.append([nx, ny])

N, M = map(int, input().split())
roadmap = [list(map(int, input())) for _ in range(N)]
bfs(0, 0)
print(roadmap[N-1][M-1])