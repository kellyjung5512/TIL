# 인접 행렬 - 재귀
# s1(인접 행렬 스택)과 메모리 차이는 없고, 시간이 아주 조금 차이남
# s1 = 84ms, s2 = 80ms -> 최대한 재귀를 사용하는게 가장 좋겠다.

import sys
sys.stdin = open('input.txt')

def dfs(v):
    if not visited[v]:
        visited[v] = 1

        for i in range(1, V+1):
            if G[v][i] == 1 and not visited[i]:
                dfs(i)
    result = sum(visited) - 1
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