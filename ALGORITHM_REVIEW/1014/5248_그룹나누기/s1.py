import sys
sys.stdin = open('input.txt', 'r')

def dfs(num):
    stack = []
    stack.append(num)

    while stack:
        p = stack.pop()
        for j in team[p]:
            if visited[j] == 0:
                stack.append(j)
                visited[j] = 1

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    member = list(map(int, input().split()))
    team = [[] for _ in range(N+1)]
    for i in range(0, len(member), 2):
        team[member[i]].append(member[i+1])
        team[member[i+1]].append(member[i])
    visited = [0] * (N+1)
    cnt = 0
    for i in range(len(team)):
        if not visited[i]:
            visited[i] = 1
            cnt += 1
            dfs(i)

    print('#{} {}'.format(tc, cnt-1))
