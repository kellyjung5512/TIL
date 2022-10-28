import sys
sys.stdin = open("input.txt")

N = int(input())
houses = [list(map(int, input())) for _ in range(N)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(a, b):
    stack = [(a, b)]
    cnt = 1
    while stack:
        x, y = stack.pop()
        houses[x][y] = 0
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < N:
                if houses[nx][ny] == 1:
                    stack.append((nx, ny))
                    houses[nx][ny] = 0
                    cnt += 1
    return cnt

result = []
for i in range(N):
    for j in range(N):
        # print(i, j)
        if houses[i][j] == 1:
            n = dfs(i, j)
            result.append(n)
result.sort()
print(len(result))
for c in range(len(result)):
    print(result[c])