import sys
from collections import deque
sys.stdin = open("input.txt")

V, E = map(int, input().split())

node = list(map(int, input().split()))
connect = [[] for _ in range(V+1)]
visited = []
for i in range(E):
    connect[node[i * 2]].append(node[(i * 2) + 1])
    connect[node[(i * 2) + 1]].append(node[i * 2])

def bfs(n):
    queue = deque()
    queue.append(n)
    while queue:
        v = queue.popleft()
        if v not in visited:
            visited.append(v)
            for a in connect[v]:
                if a not in visited:
                    queue.append(a)
    return visited

print(bfs(1))