import sys
sys.stdin = open('input.txt')

def bfs(v):
    Q = [v]
    while Q:
        num = Q.pop(0)
        if not visited[num]:
            visited[num] = 1
            print(num)

            for j in range(V+1):
                if G[num][j] == 1 and not visited[j]:
                    Q.append(j)



V, E = map(int, input().split())
temp = list(map(int, input().split()))

G = [[0 for _ in range(V+1)] for _ in range(V+1)]

for i in range(len(temp)//2):
    G[temp[i*2]][temp[i*2+1]] = 1
    G[temp[i*2+1]][temp[i*2]] = 1

visited = [0 for _ in range(V+1)]

bfs(1)