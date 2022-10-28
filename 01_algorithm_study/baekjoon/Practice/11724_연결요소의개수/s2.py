import sys
sys.stdin = open("input.txt")


N, M = map(int, sys.stdin.readline().split())
connection = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    connection[u].append(v)
    connection[v].append(u)

def dfs(L):
    stack = L
    while stack:
        v = stack.pop()
        if connection[v]:
            for j in range(len(connection[v])):
                stack.append(connection[v][j])
            connection[v] = []
            visited[v] = 1

cnt = 0
visited = [0] * (N + 1)
for i in range(1, len(connection)):
    if visited[i] == 0:
        if len(connection[i]) > 0:
            dfs(connection[i])
            cnt += 1

        else:
            cnt += 1
            visited[i] = 1

print(cnt)