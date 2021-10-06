import sys
sys.stdin = open('input.txt')

def dfs(v):
    if not visited[v]:
        visited[v] = 1
        print(v, end=' ')
        G[v].sort()
        for i in G[v]:
            if not visited[i]:
                dfs(i)

def bfs(v):
    Q = [v]
    while Q:
        x = Q.pop(0)
        if not visited[x]:
            visited[x] = 1
            print(x, end=' ')
            for i in G[x]:
                if not visited[i]:
                    Q.append(i)

N, M, V = map(int, input().split())
temp = [list(map(int, input().split())) for m in range(M)]
# print(temp)
G = [[] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]
for i in range(len(temp)):
    G[temp[i][0]].append(temp[i][1])
    G[temp[i][1]].append(temp[i][0])
# print(G)
dfs(V)
print()
visited = [0 for _ in range(N+1)]
bfs(V)