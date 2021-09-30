import sys
sys.stdin = open('input.txt')

def bfs(v):
    Q = [v]
    while Q:
        num = Q.pop(0)
        if num not in visited:
            visited.append(num)
            for i in G[num]:
                Q.append(i)

    return visited 


V, E = map(int, input().split())
temp = list(map(int, input().split()))

G = [[] for _ in range(V+1)]
for i in range(len(temp)//2):
    G[temp[i*2]].append(temp[i*2+1])
print(G)

visited = []

print(bfs(1))