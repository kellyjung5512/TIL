import sys
sys.stdin = open('input.txt')

def dfs(v):
    stack = [v]
    while stack:
        temp = stack.pop()
        if not visited[temp]:
            visited[temp] = 1
            for i in line[temp]:
                if visited[i] == 0:
                    stack.append(i)

for _ in range(10):
    tc, road = map(int, input().split())
    line = [[] for _ in range(100)]
    info = list(map(int, input().split()))
    for i in range(road):
        line[info[2*i]].append(info[2*i+1])
        # line[info[2*i+1]].append(info[2*i])
    # print(line)
    visited = [0 for _ in range(100)]
    dfs(0)
    # print(visited)
    if visited[99] == 1:
        print('#{} {}'.format(tc, 1))
    else:
        print('#{} {}'.format(tc, 0))