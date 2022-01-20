import sys
sys.stdin = open('input.txt')


def dfs(num, depth):
    global result

    if result < depth:
        result = depth

    for j in new_list[num]:
        if not visited[j]:
            visited[j] = 1
            dfs(j, depth + 1)
            visited[j] = 0


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    grape = [list(map(int, input().split())) for _ in range(M)]
    new_list = [[] for _ in range(N)]
    result = 1
    if N > 1:
        for i in range(len(grape)):
            new_list[grape[i][0]-1].append(grape[i][1]-1)
            new_list[grape[i][1]-1].append(grape[i][0]-1)
        visited = [0] * N
        for node in range(len(new_list)):
            visited[node] = 1
            dfs(node, 1)
            visited[node] = 0
    else:
        pass
    print('#{} {}'.format(tc, result))