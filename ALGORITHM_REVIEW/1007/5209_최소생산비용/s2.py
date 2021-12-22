import sys
sys.stdin = open('input.txt')

def dfs(x):
    global ans, result
    if x == N:
        if ans < result:
            result = ans
        return

    if result < ans:
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            ans += costs[x][i]
            dfs(x+1)
            ans -= costs[x][i]
            visited[i] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    costs = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    ans = 0
    result = 987654321
    dfs(0)

    print('#{} {}'.format(tc, result))