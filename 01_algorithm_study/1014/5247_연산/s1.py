from collections import deque
import sys
sys.stdin = open('input.txt')


def bfs(num):
    visited = [0] * 1000001
    visited[num] = 1
    q = deque()
    q.append(num)

    while q:
        p = q.popleft()

        if p == M:
            return visited[p] - 1

        for n in [p+1, p-1, p*2, p-10]:
            if 0 < n <= 1000000 and visited[n] == 0:
                q.append(n)
                visited[n] = visited[p] + 1


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    answer = bfs(N)

    print('#{} {}'.format(tc, answer))