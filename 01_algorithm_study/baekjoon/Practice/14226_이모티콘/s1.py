import sys
from collections import deque
sys.stdin = open('input.txt')

n = int(input())
arr = [[-1] * (n+1) for _ in range(n+1)]
q = deque()
q.append((1,0))  # 화면 이모티콘 개수, 클립보드 이모티콘 개수
arr[1][0] = 0

while q:
    s,c = q.popleft()
    if arr[s][s] == -1:
        arr[s][s] = arr[s][c] + 1
        q.append((s,s))
    if s+c <= n and arr[s+c][c] == -1:
        arr[s+c][c] = arr[s][c] + 1
        q.append((s+c, c))
    if s-1 >= 0 and arr[s-1][c] == -1:
        arr[s-1][c] = arr[s][c] + 1
        q.append((s-1, c))

ans = -1
for i in range(n+1):
    if arr[n][i] != -1:
        if ans == -1 or ans > arr[n][i]:
            ans = arr[n][i]

print(ans)