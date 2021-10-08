import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit()
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(r, c):
    global result, cnt
    cnt += 1

    if r+1 == N and c+1 == M:
        if cnt > result:
            result = cnt

    if visited[r][c] == 0:
        visited[r][c] = 1

        for i in range(4):
            nx = dx[i] + r
            ny = dy[i] + c

            if 0 <= nx < N and 0 <= ny < M and trash_map[nx][ny] == 1 and visited[nx][ny] == 0:
                dfs(nx, ny)
    return cnt

N, M, K = map(int, input().split()) # 가로가 M, 세로가 N, 쓰레기 개수 K
trash = [list(map(int, input().split())) for _ in range(K)]
trash_map = [[0 for _ in range(M)] for _ in range(N)]
for l in range(K):
    trash_map[trash[l][0]-1][trash[l][1]-1] = 1
visited = [[0 for _ in range(M)] for _ in range(N)]
cnt = 0
result = 0
for i in range(N):
    for j in range(M):
        if trash_map[i][j] == 1:
            dfs(i, j)
            if cnt > result:
                result = cnt
            cnt = 0
print(result)