import sys
sys.stdin = open('input.txt', 'r')

def dfs(v):
    visited[v] = 1
    print(v, end=' ')
    for i in range(1, N+1):
        if G[v][i] == 1 and not visited[i]:
            dfs(i)

def bfs(v):
    visited = [0 for _ in range(N + 1)]
    Q = [v]
    while Q:
        num = Q.pop(0)
        if not visited[num]:
            visited[num] = 1
            print(num, end=' ')
            for i in range(N+1):
                if G[num][i] == 1 and not visited[i]:
                    Q.append(i)

N, M, V = map(int, input().split())
edge = [list(map(int, input().split())) for _ in range(M)]
G = [[0 for _ in range(N+1)] for _ in range(N+1)]
for i in range(0, len(edge)):
    G[edge[i][0]][edge[i][1]] = 1
    G[edge[i][1]][edge[i][0]] = 1
visited = [0 for _ in range(N+1)]
dfs(V)
print()

bfs(V)