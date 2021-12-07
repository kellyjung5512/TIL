import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    color = [list(map(int, input().split())) for _ in range(N)]
    paper = [[0] * 10 for _ in range(10)]
    cnt = 0

    for i in range(len(color)):
        for j in range(color[i][0], color[i][2]+1):
            for k in range(color[i][1], color[i][3]+1):
                paper[j][k] += color[i][4]
                # if paper[j][k] >= 3:
                #     cnt += 1

    for l in range(len(paper)):
        for m in range(len(paper)):
            if paper[l][m] >= 3:
                cnt += 1

    print('#{} {}'.format(tc, cnt))