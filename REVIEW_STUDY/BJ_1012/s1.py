import sys
sys.setrecursionlimit(10000)
sys.stdin = open('input.txt')

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def dfs(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < M:   # 땅을 나가지 않는 선에서만
            if land[nx][ny] == 1:         # 돌면서 1이 있으면 0으로 바꾸고 그 부분을 또 재귀로 들어가기
                land[nx][ny] = 0
                dfs(nx, ny)

T = int(input())
for tc in range(1, T+1):
    M, N, K = map(int, input().split())
    land = [[0] * M for _ in range(N)]

    for i in range(K):                     # 배추 위치 지정
        x, y = map(int, input().split())
        land[y][x] = 1

    cnt = 0
    for j in range(N):                     # 반복문을 돌면서 필요한 배추흰지렁이 마리 수 구하기
        for k in range(M):
            if land[j][k] == 1:
                dfs(j, k)
                cnt += 1
    print(cnt)
