# 인접 행렬 - 스택

import sys
sys.stdin = open('input.txt')

def dfs(v):
    stack = [v]
    while stack:
        num = stack.pop(0)
        if not visited[num]:
            visited[num] = 1
            for i in range(1, V+1):
                if G[num][i] == 1 and not visited[i]:
                    stack.append(i)

    result = sum(visited)-1
    return result

V = int(input())
E = int(input())
computer = [list(map(int, input().split())) for _ in range(E)]
G = [[0 for _ in range(V+1)] for _ in range(V+1)]
for i in range(len(computer)):
    G[computer[i][0]][computer[i][1]] = 1
    G[computer[i][1]][computer[i][0]] = 1
visited = [0 for _ in range(V+1)]
print(dfs(1))
