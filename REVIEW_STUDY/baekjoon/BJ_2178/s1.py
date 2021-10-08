import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(10000)

def dfs(a, b):
    global cnt
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    miro[a][b] = 0
    cnt += 1
    if a == N-1 and b == M-1:
        result.append(cnt)


    else:
        for i in range(4):
            nx = dx[i] + a
            ny = dy[i] + b

            if 0 <= nx < N and 0 <= ny < M and miro[nx][ny] == 1:
                dfs(nx, ny)
                miro[nx][ny] = 1
                cnt -= 1


N, M = map(int, input().split())
miro = [list(map(int, input())) for _ in range(N)]
cnt = 0
result = []
dfs(0, 0)
print(min(result))
# print(cnt)