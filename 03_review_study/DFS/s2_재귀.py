import sys
sys.stdin = open('input.txt')

def dfs(v):
    if not visited[v]:
        visited[v] = 1
        print('{} {}'.format(v, visited))

        for j in range(V+1):
            if G[v][j] == 1 and not visited[j]:
                dfs(j)


V, E = map(int, input().split())
temp = list(map(int, input().split()))
G = [[0 for _ in range(V+1)] for _ in range(V+1)]
visited = [0 for _ in range(V+1)]

for i in range(E):
    G[temp[2*i]][temp[2*i+1]] = 1
    G[temp[2*i+1]][temp[2*i]] = 1

dfs(1)