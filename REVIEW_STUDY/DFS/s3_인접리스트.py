import sys
sys.stdin = open('input.txt')

def dfs(v):
    visited[v] = 1
    print('{} {}'.format(v, visited))
    for j in G[v]:
        if not visited[j]:
            dfs(j)

V, E = map(int, input().split())
temp = list(map(int, input().split()))
G = [[] for _ in range(V+1)]
visited = [0 for _ in range(V+1)]

for i in range(0, len(temp)-1, 2):
    G[temp[i]].append(temp[i+1])
    G[temp[i+1]].append(temp[i])

dfs(1)