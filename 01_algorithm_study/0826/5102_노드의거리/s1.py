import sys
sys.stdin = open('input.txt')

def bfs(start, end):
    Q = [[start, 0]]

    while Q:
        temp, distance = Q.pop(0)
        if temp == end:
            return distance

        visited.append(temp)

        if connection[temp]:
            for j in range(len(connection[temp])):
                if not connection[temp][j] in visited:
                    Q.append([connection[temp][j], distance+1])

    return 0

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    node = [list(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split())
    connection = [[] for _ in range(V+1)]
    # print(node)
    for i in range(len(node)):
        connection[node[i][0]].append(node[i][1])
        connection[node[i][1]].append(node[i][0])
    visited = []
    print('#{} {}'.format(tc, bfs(S, G)))
    # print(connection)

