def dfs(v):
    visited.append(v)
    for j in connect[v]:
        if j not in visited:
            dfs(j)

computer = int(input())
node = int(input())
connect = [[] for _ in range(computer+1)]
for i in range(node):
    start, end = map(int, input().split())
    connect[start].append(end)
    connect[end].append(start)
visited = []
dfs(1) # 항상 1번부터 번호 매김
print(len(visited)-1)