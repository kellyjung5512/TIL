import sys
sys.stdin = open('input.txt')
from collections import deque

def dfs(v):
    if v not in visited:
        visited.append(v)
        print(v, end=' ')
        my_list[v].sort()
        for i in my_list[v]:
            dfs(i)

def bfs(v):
    queue = deque()
    queue.append(v)
    while queue:
        num = queue.popleft()
        if num not in visited:
            visited.append(num)
            print(num, end=' ')

            for i in my_list[num]:
                queue.append(i)

N, M, V = map(int, input().split())
visited = []
my_list = [[] for _ in range(N+1)]
for i in range(M):
    x, y = map(int, input().split())
    my_list[x].append(y)
    my_list[y].append(x)
# print(my_list)
dfs(V)
visited = []
print()
bfs(V)