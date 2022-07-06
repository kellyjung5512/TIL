import sys
sys.stdin = open('input.txt')

N = int(input()) # 전체 사람의 수
info = [list(map(int, input().split())) for _ in range(N)]
ans = []

for i in range(N):
    cnt = 1
    for j in range(N):
        if info[i][0] < info[j][0] and info[i][1] < info[j][1]:
            cnt += 1
    ans.append(cnt)
print(*ans)