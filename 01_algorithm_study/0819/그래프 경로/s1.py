import sys
sys.stdin = open('input.txt')

def is_true(arr, start, end):
    stack = [start]

    while stack:
        temp = stack.pop()

        if visited[temp] != 1:
            visited[temp] = 1

            for i in arr[temp]:
                if not visited[i]:
                    stack.append(i)

    return visited[end]


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    grape = [list(map(int, input().split())) for _ in range(E)]
    check = [[] for _ in range(V+1)]
    for i in range(len(grape)):
        check[grape[i][0]].append(grape[i][1])
    visited = [0] * (V+1)
    # print(check)
    S, G = map(int, input().split())
    ans = is_true(check, S, G)
    print('#{} {}'.format(tc, ans))
