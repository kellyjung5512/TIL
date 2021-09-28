import sys
sys.stdin = open('input.txt')

def dfs(v):
    stack = [v]

    while stack:
        v = stack.pop()
        
        if visited[v] == 0:
            visited[v] = 1
            print('{} {}'.format(v, visited))

            for j in range(V+1):
                if G[v][j] == 1 and not visited[j]:
                    stack.append(j)

V, E = map(int, input().split())
# print(V, E)

temp = list(map(int, input().split()))
# print(temp)

G = [[0 for _ in range(V+1)] for _ in range(V+1)]
# print(G)

for i in range(E):
    G[temp[2*i]][temp[2*i+1]] = 1
    G[temp[2*i+1]][temp[2*i]] = 1
# print(G)

visited = [0 for _ in range(V+1)]
# print(visited)

dfs(1)
