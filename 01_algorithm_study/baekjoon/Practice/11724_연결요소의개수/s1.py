import sys
sys.stdin = open("input.txt")

def dfs(start, depth):

    visited[start] = 1

    for j in graph[start]:
        if not visited[j]:
            dfs(j, depth + 1)


N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [0] * (1 + N)
count = 0

for i in range(1, N + 1):
    if not visited[i]:
        if not graph[i]:
            count += 1
            visited[i] = 1
        else:
            dfs(i, 0)
            count += 1

print(count)