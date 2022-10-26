import sys
sys.stdin = open("input.txt")

N, M, V = map(int, input().split())
connect = [[] for _ in range(N + 1)]
dfs_visited = []
bfs_visited = []

for i in range(M):
    x, y = map(int, input().split())
    connect[x].append(y)
    connect[y].append(x)

def dfs(v):
    if v not in dfs_visited:
        dfs_visited.append(v)
        connect[v].sort()
        for j in connect[v]:
            dfs(j)

def bfs(v):
    Q = [v]
    while Q:
        tmp = Q.pop(0)
        if tmp not in bfs_visited:
            bfs_visited.append(tmp)
            connect[tmp].sort()
            for k in connect[tmp]:
                if k not in bfs_visited:
                    Q.append(k)

dfs(V)
bfs(V)
print(*dfs_visited)
print(*bfs_visited)