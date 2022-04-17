import sys
from collections import deque
sys.stdin= open('input.txt')

n, k = map(int, input().split()) # n = 수빈이의 위치, k = 동생의 위치

queue = deque()
queue.append(n)

visited = [0] * 100001

cnt = 0
way = 0
while queue:
    x = queue.popleft()
    a = visited[x]
    if x == k:
        cnt = a
        way += 1
        continue

    for nx in [x-1, x+1, 2*x]:
        if 0 <= nx < 100001:
            if visited[nx] == 0 or visited[nx] == visited[x] + 1:
                queue.append(nx)
                visited[nx] = a + 1
                

print(cnt)
print(way)