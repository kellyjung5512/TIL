import sys
sys.stdin = open('input.txt')

def dfs(x, ans):
    global result
    if result >= ans:
        return

    if x == N:
        if result < ans:
            result = ans
        return

    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            dfs(x + 1, ans * percent[x][i] * 0.01)
            visited[i] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    percent = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    result = 0
    dfs(0, 1)

    print('#{} {:.6f}'.format(tc, result*100))