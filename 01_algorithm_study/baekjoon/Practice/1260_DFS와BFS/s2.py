import sys
from collections import deque
sys.stdin = open("input.txt")

N, M, V = map(int, input().split())

# node 생성
node = [[] for _ in range(N+1)]

# 방문체크
dfs_visited = []
bfs_visited = []

for _ in range(M):
    a, b = map(int, input().split())
    node[a].append(b)
    node[b].append(a)

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


dfs(V)
print()
bfs(V)