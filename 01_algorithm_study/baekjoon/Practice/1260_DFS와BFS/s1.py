import sys
from collections import deque
sys.stdin = open('input.txt')

def dfs(v):
    if v not in dfs_visited:
        dfs_visited.append(v)
        print(v, end=" ")
        node[v].sort()
        for i in node[v]:
            dfs(i)

def bfs(v):
    queue = deque()
    queue.append(v)
    while queue:
        num = queue.popleft()
        if num not in bfs_visited:
            bfs_visited.append(num)
            print(num, end=" ")
            for i in node[num]:
                queue.append(i)

N, M, V = map(int, input().split())
dfs_visited = []
bfs_visited = []
node = [[] for _ in range(N+1)]
for _ in range(M):
    x, y = map(int, input().split())
    node[x].append(y)
    node[y].append(x)

dfs(V)
print()
bfs(V)