import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(10**6)     ## 재귀를 풀 때는 선택 아닌 필수 코드...!
dx = [-1, 0, 1, 0, -1, -1, 1, 1]
dy = [0, 1, 0, -1, -1, 1, -1, 1]

def dfs(x, y):
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < h and 0 <= ny < w and grape[nx][ny] == 1:
            grape[nx][ny] = 0
            dfs(nx, ny)

while True:     # n회라는게 없을 때 어떻게 하는지 이제 알았음 ㅋㅋ..!
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    grape = [list(map(int, input().split())) for _ in range(h)]
    cnt = 0
    for i in range(h):
        for j in range(w):
            if grape[i][j] == 1:
                cnt += 1
                grape[i][j] = 0
                dfs(i, j)
    print(cnt)
