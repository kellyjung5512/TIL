import sys
sys.stdin = open('input.txt', encoding='utf-8')

dr = [1, 1, -1, -1]
dc = [-1, 1, 1, -1]

def find_dessert(c, r):

    for k in range(4):
        nr = dr[k] + r
        nc = dc[k] + c


        if k < 2:
            if 0 <= nr < N and 0 <= nc < N and not dessert[nc][nr] in visited:
                visited.append(dessert[nc][nr])
                if k % 2:
                    delta[0] += 1
                else:
                    delta[1] += 1
            else:
                return
    pass

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    dessert = [list(map(int, input().split())) for _ in range(N)]
    for i in range(1, N-1):
        for j in range(N):
            delta = [0, 0]
            visited = []
            find_dessert(i, j)
